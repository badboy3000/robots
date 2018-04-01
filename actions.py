import random
import time

from tie import get_driver, post_tei

wait = [25, 30, 35, 40, 45, 50, 55]

post_urls = [
    'https://tieba.baidu.com/p/5605886801',  # 寄生兽（顶不起来）
    'https://tieba.baidu.com/p/5605900661',  # 七大罪（顶不起来）
    'https://tieba.baidu.com/p/5605905061',  # 东京食尸鬼（顶不起来）
    'https://tieba.baidu.com/p/5605911029',  # 从零开始的异界生活（顶不起来）
    'https://tieba.baidu.com/p/5607203905',  # 刀剑神域
    'https://tieba.baidu.com/p/5607225158',  # 博多豚骨拉面
    'https://tieba.baidu.com/p/5607240021',  # 一拳超人
    'https://tieba.baidu.com/p/5619888373',  # 叛逆的鲁鲁修
    'https://tieba.baidu.com/p/5622324258',  # CLANNAD
    'https://tieba.baidu.com/p/5622219287',  # 黑执事
    'https://tieba.baidu.com/p/5621745503',  # 叛逆的鲁鲁修
    'https://tieba.baidu.com/p/5628999264',  # darling in the frankxx
]

contents = [
    '咖喱棒tv~天下漫友是一家，加油哦！希望以后越来越好！',
    'calibur...不错呢，如果是excalibur就更赞了！',
    '楼主这么多资源从哪搞来的啊？签到还送金币？em......',
    '哇，大佬！看上去很棒哎，加油加油，以后看番就不愁了',
    '6666666，不知道会不会被禁呐，小心点为好吧，楼主加油。',
    '强~无敌！有我喜欢的资源~~，楼主加油！希望越来越好',
    '....我去这么多资源不怕被禁吗？闷声发大财啊楼主！'
]

driver = get_driver()

while 1:
    try:
        post_url = random.choice(post_urls)
        content = random.choice(contents)
        post_tei(driver, post_url, content)

        time.sleep(random.choice(wait))
    except Exception as err:
        print(err)
