from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
import time, winsound, logging

driver = webdriver.Chrome('/driver/chromedriver')
driver.get('https://lol.gamepedia.com/OnGameNet')

for clickable in driver.find_elements_by_class_name('mw-collapsible-text'):
    clickable.click()

leagues = [link.get_attribute('href') for link in driver.find_elements_by_xpath('//td[@class="navbox-group" and text()="Champions"]/../td//a')]
league_done = ['https://lol.gamepedia.com/Azubu_The_Champions_Spring_2012', 'https://lol.gamepedia.com/Azubu_The_Champions_Summer_2012', 'https://lol.gamepedia.com/Season_3_Korea_Regional_Finals', 'https://lol.gamepedia.com/2014_Season_Korea_Regional_Finals', 'https://lol.gamepedia.com/Champions_Spring_2015/Qualifiers', 'https://lol.gamepedia.com/Champions_Spring_2015/Preseason', 'https://lol.gamepedia.com/SBENU_Champions_Spring_2015', 'https://lol.gamepedia.com/SBENU_Champions_Spring_2015_Playoffs', 'https://lol.gamepedia.com/SBENU_Champions_Summer_2015/Promotion', 'https://lol.gamepedia.com/SBENU_Champions_Summer_2015', 'https://lol.gamepedia.com/SBENU_Champions_Summer_2015_Playoffs', 'https://lol.gamepedia.com/2015_Season_Korea_Regional_Finals', 'https://lol.gamepedia.com/LCK/2016_Season/Spring_Promotion', 'https://lol.gamepedia.com/LCK/2016_Season/Spring_Season', 'https://lol.gamepedia.com/LCK/2016_Season/Spring_Playoffs', 'https://lol.gamepedia.com/LCK/2016_Season/Summer_Promotion', 'https://lol.gamepedia.com/LCK/2016_Season/Summer_Season', 'https://lol.gamepedia.com/LCK/2016_Season/Summer_Playoffs', 'https://lol.gamepedia.com/2016_Season_Korea_Regional_Finals', 'https://lol.gamepedia.com/LCK/2017_Season/Spring_Promotion', 'https://lol.gamepedia.com/LCK/2017_Season/Spring_Season', 'https://lol.gamepedia.com/LCK/2017_Season/Spring_Playoffs', 'https://lol.gamepedia.com/LCK/2017_Season/Summer_Promotion', 'https://lol.gamepedia.com/LCK/2017_Season/Summer_Season', 'https://lol.gamepedia.com/LCK/2017_Season/Summer_Playoffs', 'https://lol.gamepedia.com/2017_Season_Korea_Regional_Finals', 'https://lol.gamepedia.com/LCK/2018_Season/Spring_Promotion', 'https://lol.gamepedia.com/LCK/2018_Season/Spring_Season', 'https://lol.gamepedia.com/LCK/2018_Season/Spring_Playoffs', 'https://lol.gamepedia.com/LCK/2018_Season/Summer_Promotion', 'https://lol.gamepedia.com/LCK/2018_Season/Summer_Season', 'https://lol.gamepedia.com/LCK/2018_Season/Summer_Playoffs', 'https://lol.gamepedia.com/LCK/2018_Season/Regional_Finals', 'https://lol.gamepedia.com/LCK/2019_Season/Spring_Promotion']
league_passed = ['https://lol.gamepedia.com/OLYMPUS_Champions_Winter_2012-2013', 'https://lol.gamepedia.com/OLYMPUS_Champions_Spring_2013', 'https://lol.gamepedia.com/HOT6iX_Champions_Summer_2013', 'https://lol.gamepedia.com/PANDORA.TV_Champions_Winter_2013-2014', 'https://lol.gamepedia.com/HOT6iX_Champions_Spring_2014', 'https://lol.gamepedia.com/HOT6iX_Champions_Summer_2014']

try:
    with open('gamepedia.txt','a',encoding='utf-8') as f:
        for league in leagues:
            if league in league_done or league in league_passed:
                continue
            driver.get(league)
            try:
                driver.find_element_by_xpath('//a[text()="Scoreboards"]').click()
                time.sleep(0.1)
            except Exception:
                league_passed.append(league)
                continue

            last_tab = driver.find_elements_by_class_name('tabheader-top')[-1]
            tabs = [None]
            try:
                last_tab.find_element_by_xpath('.//a[text()="Scoreboards"]')
            except Exception:
                tabs = [tab.get_attribute('href') for tab in last_tab.find_elements_by_xpath('.//a')]
            for tab in tabs:
                if tab is not None:
                    driver.get(tab)
                for i in range(10):
                    try:
                        driver.find_element_by_id('toggler0').click()
                        time.sleep(0.1)
                    except ElementNotVisibleException:
                        break
                    except Exception:
                        pass
                
                title = driver.find_element_by_id('firstHeading').text
                print(title)
                matches = driver.find_elements_by_class_name('matchrecap1')
                if len(matches) == 0:
                    matches = driver.find_elements_by_xpath('//div[@class="inline-content"]/table[contains(@class,"matchrecap")]')
                for table in matches:                    
                    boards = table.find_elements_by_xpath('.//table[contains(@class, "matchrecap")]')
                    page_type = 2 if len(table.find_elements_by_xpath('.//b[contains(text(), "Length:")]')) > 0 else 1
                    if page_type != 2:
                        page_type = 3 if len(boards[0].find_elements_by_xpath('.//b[contains(text(), "Bans")]')) > 0 else 1
                    tds = boards[0].find_elements_by_xpath('.//td')
                    if page_type == 3:
                        team_line =  boards[0].find_elements_by_class_name('matchrecapScoreLine')
                        win = 'background-color' in [td for td in team_line if len(td.text) == 1][0].get_attribute('style')
                        teams = [team_line[0].text, team_line[-1].text]
                        bans = [img.get_attribute('alt')[:-10] for img in boards[0].find_elements_by_xpath('.//td[@class="matchrecapBans"]//img')]
                        times = boards[0].find_element_by_xpath('.//td[contains(text(),":")]').text.split(':')
                        date = boards[4].find_element_by_class_name('DateInLocalSB').text.replace('Date: ','')
                    else:
                        team_line =  boards[0].find_elements_by_class_name('matchrecapScoreLine')
                        win = 'background-color' in [td for td in team_line if len(td.text) == 1][0].get_attribute('style')
                        teams = [tds[0].text, tds[-1].text]
                        bans = [img.get_attribute('alt')[:-10] for img in boards[1].find_element_by_xpath('.//tr').find_elements_by_xpath('.//img')]
                        if page_type == 1:
                            # type 1
                            times = boards[1].find_elements_by_xpath('.//td')[-6].text.split(':')
                            date = boards[4].find_element_by_class_name('DateInLocalSB').text.replace('Date: ','')
                        else:
                            # type 2
                            times = table.find_element_by_xpath('.//b[contains(text(), "Length:")]/..').text[8:].split(':')
                            date = table.find_element_by_xpath('.//b[contains(text(), "Length:")]/../../td').text.replace('Date: ','')
                    try:
                        times = int(times[0]) * 60 + int(times[1])
                    except IndexError:
                        times = int(times[0]) * 60
                    # date = table.find_element_by_class_name('DateInLocalSB').text
                    if page_type == 1:
                        # type 1
                        for i, player in enumerate(boards[3].find_elements_by_xpath('.//table[contains(@class,"wikitable")]')):
                            champ = player.find_element_by_xpath('.//img').get_attribute('alt')[:-10]
                            tds = player.find_elements_by_xpath('.//td')                
                            name = tds[1].text                                
                            name_link = tds[1].find_element_by_xpath('.//a').get_attribute('href')
                            spell1, spell2 = [td.find_element_by_xpath('./a').get_attribute('href').split('/')[-1].lower() for td in tds[2:4]]
                            kill, death, assist = [td.text for td in  tds[4:7]]
                            gold, cs = [td.text for td in  tds[-2:]]
                            team = teams[i%2]
                            team_win = win if i%2 == 0 else not win
                            f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(date, title, times, team, team_win, name, name_link, champ, kill, death, assist, gold, cs, spell1, spell2, ','.join(bans)))
                    elif page_type == 2:
                        # type 2
                        for board in boards[4:6]:
                            i = 0 if board == boards[4] else 1
                            for player in board.find_elements_by_xpath('.//table[contains(@class,"wikitable")]'):                    
                                champ = player.find_element_by_xpath('.//img').get_attribute('alt')[:-10]
                                tds = player.find_elements_by_xpath('.//td')
                                name = tds[1].text
                                name_link = tds[1].find_element_by_xpath('.//a').get_attribute('href')
                                spell1, spell2 = [td.find_element_by_xpath('./img').get_attribute('alt').split('(')[0].strip().lower() for td in tds[2:4]]                                    
                                kill, death, assist = [td.text for td in tds[4:] if td.text.strip().isdigit()][:3]
                                gold, cs = [td.text for td in  tds[-2:]]
                                team = teams[i]
                                team_win = win if i == 0 else not win
                                f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(date, title, times, team, team_win, name, name_link, champ, kill, death, assist, gold, cs, spell1, spell2, ','.join(bans)))
                    else:
                        # type 3
                        for board in boards[2:4]:
                            i = 0 if board == boards[2] else 1
                            for player in board.find_elements_by_xpath('.//table[contains(@class,"wikitable")]'):                    
                                champ = player.find_element_by_xpath('.//img').get_attribute('alt')[:-10]
                                tds = player.find_elements_by_xpath('.//td')
                                name = tds[1].text
                                name_link = tds[1].find_element_by_xpath('.//a').get_attribute('href')
                                spell1, spell2 = [td.find_element_by_xpath('./img').get_attribute('alt').split('(')[0].strip().lower() for td in tds[2:4]]                                    
                                kill, death, assist = [td.text for td in tds[4:] if td.text.strip().isdigit()][:3]
                                gold, cs = [td.text for td in  tds[-2:]]
                                team = teams[i]
                                team_win = win if i == 0 else not win
                                f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(date, title, times, team, team_win, name, name_link, champ, kill, death, assist, gold, cs, spell1, spell2, ','.join(bans)))

            league_done.append(league)

    driver.close()

except Exception as e:
    logging.error(e, exc_info=True)
    for i in range(3):
        winsound.Beep(1000, 1000)

print(league_passed)
print(league_done)
