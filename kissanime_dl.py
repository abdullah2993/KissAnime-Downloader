"""
Download anime from http://KissAnime.to
"""
from argparse import ArgumentParser
import base64
import bs4
import cfscrape
import wget
import re

BASE_LINK = 'http://kissanime.ru'

# name = raw_input('Anime Name:')

class KissAnime(object):
    """
    KissAnime Handler
    """
    def __init__(self, link):
        self.scraper = cfscrape.create_scraper()
        source = self.scraper.get(link).content.decode('utf-8')
        soup_s = bs4.BeautifulSoup(source, 'html.parser')
        trs = reversed(soup_s('table')[0].findAll('tr')[2:])
        self.episodes = list(KissAnime.__trs_process(trs))
        #self.episodes_data = []
        # for episode in episodes:
        #     self.episodes_data.append(self._get_ep_data(episode))

    def get_ep(self, ep_no):
        """
            get episode by Number
        """
        for current in self.episodes:
            if current['number'].__contains__(ep_no):
                return self._get_ep_data(current)

    def dl_ep(self, ep_no, quality):
        """
            Download episode
        """
        episode = self.get_ep(ep_no)
        if episode is not None:
            wget.download(episode['downloads'][quality], out=episode['title'])


    @staticmethod
    def __trs_process(trs):
        for row in trs:
            tds = row.findAll('td')
            ep_link = BASE_LINK + tds[0].a['href']
            ep_title = tds[0].a.string.strip()
            ep_date = tds[1].string
            yield {'title':ep_title, 'link':ep_link, 'data':ep_date, \
            'number':KissAnime._get_ep_no(ep_title)}

    def _get_ep_data(self, episode):
        ep_source = self.scraper.get(episode['link']).content.decode('utf-8')
        soup_e = bs4.BeautifulSoup(ep_source, 'html.parser')
        result = {"title": episode['title'], "downloads":{}}
        for opt in soup_e('select', {'id': 'selectQuality'})[0].findAll('option'):
            #print('Quality: ', opt.string)
            #print('Link: ', base64.b64decode(opt['value']))
            result["downloads"][opt.string] = base64.b64decode(opt['value'])
        return result

    @staticmethod
    def _get_ep_no(title):
        match = re.match(r".*?((?P<ep1>\d+)(-(?P<ep2>\d+))?)$", title)
        assert match
        groups = match.groupdict()
        if groups['ep2'] is not None:
            return [groups['ep1'].lstrip('0'), groups['ep2'].lstrip('0')]
        else:
            return [groups['ep1'].lstrip('0')]



def main(link):
    """
    Main script
    """
    k = KissAnime(link)
    for i in ARGS.episodes:
        k.dl_ep(i, ARGS.quality)


if __name__ == '__main__':
    PARSER = ArgumentParser(description='Download anime from KissAnime.to')
    GROUP = PARSER.add_mutually_exclusive_group(required=True)
    GROUP.add_argument("-l", "--link", help="Link to Anime")
    GROUP.add_argument("-n", "--name", help="Name of the anime")
    PARSER.add_argument("-q", "--quality", help="Video Quality",\
     choices=['360p', '480p', '720p', '1080p'], default="360p")
    PARSER.add_argument("-v", "--verbose", action="store_false")
    PARSER.add_argument("-e", "--episodes", nargs="+", type=str)
    ARGS = PARSER.parse_args()
    LINK = ARGS.link
    if ARGS.name:
        NAME_ESC = ARGS.name.replace(' ', '-')
        LINK_ANIME_REL = '/anime/' + NAME_ESC
        LINK = BASE_LINK + LINK_ANIME_REL
    main(LINK)
