from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
import time, winsound, logging

driver = webdriver.Chrome('/driver/chromedriver')
driver.get('https://lol.gamepedia.com/North_America_League_Championship_Series')

# for clickable in driver.find_elements_by_class_name('mw-collapsible-text'):
#     clickable.click()
#     time.sleep(1)

lcs = driver.find_element_by_xpath('//td[@class="navbox-group"]')
leagues = [link.get_attribute('href') for link in lcs.find_elements_by_xpath('../td//a') if link.get_attribute('href') is not None]
league_done = ['https://lol.gamepedia.com/LCS/2019_Season/Spring_Season', 'https://lol.gamepedia.com/LCS/2019_Season/Spring_Playoffs', 'https://lol.gamepedia.com/LCS/2019_Season/Summer_Season', 'https://lol.gamepedia.com/LCS/2019_Season/Summer_Playoffs', 'https://lol.gamepedia.com/index.php?title=LCS/2019_Season/Regional_Finals&action=edit&redlink=1', 'https://lol.gamepedia.com/index.php?title=2019_Season/Championship_Points&action=edit&redlink=1', 'https://lol.gamepedia.com/NA_LCS/2018_Season/Spring_Promotion', 'https://lol.gamepedia.com/NA_LCS/2018_Season/Spring_Season', 'https://lol.gamepedia.com/NA_LCS/2018_Season/Spring_Playoffs', 'https://lol.gamepedia.com/NA_LCS/2018_Season/Summer_Season', 'https://lol.gamepedia.com/NA_LCS/2018_Season/Summer_Playoffs', 'https://lol.gamepedia.com/NA_LCS/2018_Season/Regional_Finals', 'https://lol.gamepedia.com/NA_LCS/2017_Season/Spring_Promotion', 'https://lol.gamepedia.com/NA_LCS/2017_Season/Spring_Season', 'https://lol.gamepedia.com/NA_LCS/2017_Season/Spring_Playoffs', 'https://lol.gamepedia.com/NA_LCS/2017_Season/Summer_Promotion', 'https://lol.gamepedia.com/NA_LCS/2017_Season/Summer_Season', 'https://lol.gamepedia.com/NA_LCS/2017_Season/Summer_Playoffs', 'https://lol.gamepedia.com/2017_Season_North_America_Regional_Finals', 'https://lol.gamepedia.com/NA_LCS/2016_Season/Spring_Promotion', 'https://lol.gamepedia.com/NA_LCS/2016_Season/Spring_Season', 'https://lol.gamepedia.com/NA_LCS/2016_Season/Spring_Playoffs', 'https://lol.gamepedia.com/NA_LCS/2016_Season/Summer_Promotion', 'https://lol.gamepedia.com/NA_LCS/2016_Season/Summer_Season', 'https://lol.gamepedia.com/NA_LCS/2016_Season/Summer_Playoffs', 'https://lol.gamepedia.com/2016_Season_North_America_Regional_Finals', 'https://lol.gamepedia.com/NA_LCS/2015_Season/Spring_Promotion', 'https://lol.gamepedia.com/NA_LCS/2015_Season/Spring_Expansion', 'https://lol.gamepedia.com/NA_LCS/2015_Season/Spring_Season', 'https://lol.gamepedia.com/NA_LCS/2015_Season/Spring_Playoffs', 'https://lol.gamepedia.com/NA_LCS/2015_Season/Summer_Promotion', 'https://lol.gamepedia.com/NA_LCS/2015_Season/Summer_Season', 'https://lol.gamepedia.com/NA_LCS/2015_Season/Summer_Playoffs', 'https://lol.gamepedia.com/2015_Season_North_America_Regional_Finals', 'https://lol.gamepedia.com/NA_LCS/2014_Season/Spring_Promotion', 'https://lol.gamepedia.com/NA_LCS/2014_Season/Spring_Season', 'https://lol.gamepedia.com/NA_LCS/2014_Season/Spring_Playoffs', 'https://lol.gamepedia.com/NA_LCS/2014_Season/Summer_Promotion', 'https://lol.gamepedia.com/NA_LCS/2014_Season/Summer_Season', 'https://lol.gamepedia.com/NA_LCS/2014_Season/Summer_Playoffs', 'https://lol.gamepedia.com/NA_LCS/Season_3/Spring_Season', 'https://lol.gamepedia.com/NA_LCS/Season_3/Spring_Playoffs', 'https://lol.gamepedia.com/NA_LCS/Season_3/Summer_Promotion', 'https://lol.gamepedia.com/NA_LCS/Season_3/Summer_Season', 'https://lol.gamepedia.com/NA_LCS/Season_3/Summer_Playoffs']
league_passed = ['https://lol.gamepedia.com/2018_Season/Championship_Points', 'https://lol.gamepedia.com/2017_Season/Championship_Points', 'https://lol.gamepedia.com/2016_Season/Championship_Points', 'https://lol.gamepedia.com/2015_Season/Championship_Points', 'https://lol.gamepedia.com/PAX_2014', 'https://lol.gamepedia.com/NA_LCS/Season_3/Spring_Qualifiers', 'https://lol.gamepedia.com/PAX_2013']

try:
    with open('gamepedia_lcs.txt','a',encoding='utf-8') as f:
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
                        try:
                            win = 'background-color' in [td for td in team_line if len(td.text) == 1][0].get_attribute('style')
                        except Exception:
                            print('exception! in {}'.title)
                            win = True
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
                    # except ValueError:
                    #     times = ''
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
            # break

    driver.close()

except Exception as e:
    logging.error(e, exc_info=True)
    for i in range(3):
        winsound.Beep(1000, 1000)

print(league_passed)
print(league_done)
