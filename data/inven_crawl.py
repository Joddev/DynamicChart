from selenium import webdriver
import time, winsound, sys

if len(sys.argv) != 4:
    print('Expected 4 args')
    exit(0)

class Team:
    def __init__(self, name, kill, death, assist, win):
        self.players = []
        self.name = name
        self.kill = kill
        self.death = death
        self.assist = assist
        self.win = win


class Player:
    def __init__(self, name, champ, kill, death, assist):
        self.name = name
        self.champ = champ
        self.kill = kill
        self.death = death
        self.assist = assist

link = sys.argv[1]
driver = webdriver.Chrome('/driver/chromedriver')

f = open(sys.argv[3],'a',encoding='utf-8')
for i in range(int(sys.argv[2])):
    driver.get(link.format(i+1))
    for frame in driver.find_elements_by_class_name('listFrame'):
        date = frame.find_element_by_class_name('date').text
        title = frame.find_element_by_class_name('title').text
        stage = frame.find_element_by_class_name('stage').text
        teams = frame.find_elements_by_xpath('./div[contains(@class, \'Team\')]')
        game_time = [int(t[:-1]) for t in frame.find_element_by_class_name('gametime').text.split()[2:]]
        try:
            game_time = game_time[0] * 60 + game_time[1]
        except IndexError:
            game_time = game_time[0] * 60
        team_list = []
        for team in teams:
            team_name = team.find_element_by_class_name('teamname').text
            score = team.find_element_by_class_name('teamscore').find_elements_by_class_name('tx2')
            team_kill = score[0].text
            team_death = score[1].text
            team_assist = score[2].text
            team_win = team.find_element_by_class_name('rightPart').text.strip() == 'W' or team.find_element_by_class_name('leftPart').text.strip() == 'W'
            team_list.append(Team(team_name, team_kill, team_death, team_assist, team_win))
            # print(team_name, team_kill, team_death, team_assist, team_win)
        frame.find_element_by_class_name('detail').click()
        found = False
        cnt = 0
        while not found:
            time.sleep(0.1)
            cnt += 1
            if cnt > 10:
                winsound.Beep(1000, 1000)
            try:
                frame.find_element_by_class_name('detailTable')
                found = True
            except Exception:
                pass
        bans = [img.get_attribute('onmouseover')[26:-3] for img in frame.find_elements_by_xpath('.//ul[@class="ban"]//img')]
        for i, ul in enumerate(frame.find_element_by_class_name('detailTable').find_elements_by_xpath('./ul')):
            for li in ul.find_elements_by_xpath('./li'):
                champ = li.find_element_by_class_name('champicon').get_attribute('onmouseover')[26:-3]
                name = li.find_element_by_class_name('playername').text
                spell1, spell2 = [img.get_attribute('onmouseover')[26:-3] for img in li.find_elements_by_xpath('.//div[@class="spellicon"]/img')]
                score = li.find_element_by_class_name('p2').find_elements_by_xpath('./li')
                kill = score[0].text
                death = score[1].text
                assist = score[2].text            
                team_list[i].players.append(Player(name, champ, kill, death, assist))
                f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
                    date, title + ' ' + stage, game_time, team_list[i].name, team_list[i].win, name, '', champ, kill, death, assist, '', '', spell1, spell2, ','.join(bans)))
                # print(champ, name, kill, death, assist)

        # print(date, title, stage, game_time)
        # for team in team_list:
        #     for player in team.players:                
        #         f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
        #             date,title,stage,game_time,team.name,team.kill,team.death,team.assist,team.win,
        #             player.name,player.champ,player.kill,player.death,player.assist
        #         ))

f.close()
driver.close()
