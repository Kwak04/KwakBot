# client id : 547685961136603149
# token : NTQ3Njg1OTYxMTM2NjAzMTQ5.D06bTA.rqxzMYB8ErcwoMuwE1CP7THQ7kQ
# client secret : 63U9h5F9bVNXGkHXwk2LJCVCfioX6t1Y
# 노랑 : 0xffff00  청록 : 0x00ffff

import asyncio
import discord
import random
import requests
import json
from datetime import datetime


# 준비
client = discord.Client()
token = "NTQ3Njg1OTYxMTM2NjAzMTQ5.D06bTA.rqxzMYB8ErcwoMuwE1CP7THQ7kQ"
count = 0


# 로그인
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="재밌게", type=1))
    print("Successfully logged in!")
    print("%s (%s)" % (client.user.name, client.user.id))
    print("---------------------------------------")


# 서버에 메시지 출력
@client.event
async def on_message(message):

    if message.author.bot:
        return None

    # counter 함수 생성
    def counter(description):
        global count
        count += 1
        print(count, message.content, " // %s" % description)

    # 도움말
    help_keyword = ["콱봇 도와줘", "콱봇 도움말", "콱봇 도움", "콱봇 help"]
    if message.content in help_keyword:
        counter("도움말을 출력합니다.")

        # TODO 버튼식으로 넘어가게 만들기
        help_embed = discord.Embed(
            title="콱봇 도움말 :D",
            description="콱봇을 사용하는 방법에 대해서 설명합니다.",
            color=0xffffff
        )
        help_embed.add_field(
            name="도움말 보기",
            value="**콱봇 도와줘** or **콱봇 도움말** or **콱봇 help** : \n"
            "총 3가지의 방법으로 도움말을 불러오실 수 있습니다."
            ,
            inline=False
        )
        help_embed.add_field(
            name="엔터테인먼트",
            value="**콱봇 사로** or **콱봇 saro** : "
            "루프스테이션의 신 Saro의 영상을 보실 수 있습니다."
            ,
            inline=False
        )
        help_embed.add_field(
            name="선택하기",
            value="**콱봇 선택** a b c or **콱봇 골라** a b c: "
            "a, b, c 중 하나를 콱봇이 선택합니다."
            ,
            inline=False
        )
        help_embed.add_field(
            name="번역하기",
            value="**콱봇 한영번역** 어쩌구저쩌구 : "
            "입력한 한국어를 영어로 번역합니다.\n"
            "**콱봇 영한번역** blahblah : "
            "입력한 영어를 한국어로 번역합니다."
            ,
            inline=False
        )
        help_embed.add_field(
            name="시간 알려주기",
            value="**콱봇 시간** : "
            "현재 시간을 출력합니다.\n"
            "**콱봇 날짜** : "
            "오늘 날짜를 출력합니다.\n"
            "**콱봇 시간날짜** : "
            "시간과 날짜를 동시에 출력합니다."
            ,
            inline=False
        )
        help_embed.add_field(
            name="사이트 이동",
            value="**콱봇 사이트 site** : "
            "특정 사이트로 이동하는 링크를 출력합니다.\nex) 콱봇 사이트 네이버 or naver (한/영 상관없음)\n"
            "**콱봇 사이트 목록** : "
            "이동할 수 있는 사이트 목록을 확인할 수 있습니다."
        )
        help_embed.add_field(
            name="콱봇과 놀기",
            value="**콱봇 가위바위보** : "
            "콱봇과 가위바위보를 합니다.\n"
            "**콱봇 하나빼기** : "
            "콱봇과 하나빼기를 합니다.\n"
            "**콱봇 묵찌빠** : "
            "만들기 귀찮습니다."
            ,
            inline=False
        )
        help_embed.add_field(
            name="기타",
            value="**콱봇 프사** : "
            "콱봇의 프로필 사진을 보여줍니다.",
            inline=False
        )
        help_embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/547642671460515841/551420106585145359/awesome_face.png"
        )
        help_embed.set_footer(
            text="by Tronix (도움말 리뉴얼 중입니다.)",
            icon_url="https://cdn.discordapp.com/attachments/547642671460515841/549600907700994050/KakaoTalk_20190127_152958900.jpg"
        )
        await client.send_message(message.channel, embed=help_embed)

    if message.content == "콱봇 베타":
        help_beta_embed = discord.Embed(
            title="콱봇 도움말 :D",
            description="콱봇을 사용하는 방법에 대해서 설명합니다.\n"
                        "**콱봇 도와줘** or **콱봇 도움말** or **콱봇 help**\n"
                        "위의 3가지 방법으로 도움말을 불러오실 수 있습니다.",
            color=0xffffff
        )
        help_beta_embed.add_field(
            name="아래 이모지들을 눌러 관련 도움말을 펼치세요.",
            value=":clapper: 1. 엔터테인먼트\n"
            ":slot_machine: 2. 선택하기\n"
            ":notebook_with_decorative_cover: 3. 번역하기\n"
            ":alarm_clock: 4. 시간 알려주기\n"
            ":mag_right: 5. 사이트 이동\n"
            ":video_game: 6. 콱봇과 놀기\n"
            ":gear: 7. 기타"
        )
        help_beta_embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/547642671460515841/551420106585145359/awesome_face.png"
        )
        help_beta_embed.set_footer(
            text="by Tronix",
            icon_url="https://cdn.discordapp.com/attachments/547642671460515841/549600907700994050/KakaoTalk_20190127_152958900.jpg"
        )
        await client.send_message(message.channel, embed=help_beta_embed)

        help_msg = await client.send_message(message.channel, "▼")
        await client.add_reaction(help_msg, "🎬")
        await client.add_reaction(help_msg, "🎰")
        await client.add_reaction(help_msg, "📔")
        await client.add_reaction(help_msg, "⏰")
        await client.add_reaction(help_msg, "🔎")
        await client.add_reaction(help_msg, "🎮")
        await client.add_reaction(help_msg, "⚙")

        # def check(reaction, user):
        #     e = str(reaction.emoji)
        #     return e.startswith(("👍", "👎"))
        # help_res = await client.wait_for_reaction(message=help_msg, check=check, user=message.author)
        # print(help_res)

    # 일상대화 (접두사(콱봇) 없음)
    if message.content == "콱봇":
        counter("콱봇이 대답합니다.")
        await client.send_message(message.channel, random.choice(["네?", "저 부르셨어요?", "왜요?"]))

    if message.content == "콱봇 안녕":
        counter("콱봇이 인사합니다.")
        await client.send_message(message.channel, "안녕하세요 :D")
        
    if message.content == "콱봇 ㅎㅇ":
        counter("콱봇이 인사합니다.")
        await client.send_message(message.channel, "ㅎㅇ염 ㅎㅎ")

        # 반응
    # if message.content.startswith("ㅋㅋㅋㅋㅋㅋ") or message.content.endswith("ㅋㅋㅋㅋㅋㅋ"):
    #     counter("콱봇이 따라 웃습니다.")
    #     await client.send_message(message.channel, "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
    #
    # if message.content.startswith("??") or message.content.endswith("??"):
    #     counter("콱봇이 물음표를 띄웁니다.")
    #     await client.send_message(message.channel, "???")

    if message.content == "!!":
        counter("..!!!")
        await client.send_message(message.channel, "..!!!")

    if message.content == "ㅇㅋ":
        counter("오께이 좋아유~")
        await client.send_message(message.channel, "오께이 좋아유~")

    if "ㅠ" in message.content:
        counter("ㅠㅠ")
        await client.send_message(message.channel, "ㅠㅠ")

    if message.content == "엉":
        counter("엉? 덩이")
        await client.send_message(message.channel, "덩이")

    if "앙" in message.content:
        counter("앙기모띠")
        await client.send_message(message.channel, "앙기모띠")

    # 대답
    if message.content == "잘자":
        counter("콱봇이 인사합니다.")
        await client.send_message(message.channel, "안녕히 주무세요~")

    if message.content.endswith("올게"):
        counter("콱봇이 인사합니다.")
        await client.send_message(message.channel, "다녀오세요~")

    if message.content.startswith("갔다"):
        counter("콱봇이 인사합니다.")
        await client.send_message(message.channel, "다녀오셨어요?")

        # 욕 감지
    words = ["씨발", "시발", "ㅅㅂ", "좆", "병신", "ㅄ", "ㅂㅅ", "쌍", "썅", "ㅆ", "새끼"]
    for i in range(len(words)):
        if words[i] in message.content:
            counter("욕을 감지했습니다.")
            try:
                await client.delete_message(message)
            except discord.errors.NotFound:
                pass
            else:
                await client.send_message(message.channel, "<@%s>님 욕하지 마세요~~^^" % message.author.id)

    # 정보 (접두사(콱봇) 있음)
        # 인물정보
    if message.content == "콱봇 최연욱":
        counter("최연욱은 무엇일까")
        await client.send_message(message.channel, random.choice(["바부", "부바", "어부바"]))

    if message.content == "콱봇 곽현민":
        counter("곽현민?")
        await client.send_message(message.channel, "그게 누구죠;;")

    if message.content == "콱봇 안현빈":
        counter("안현빈은 무엇일까")
        await client.send_message(message.channel, "아 그 통통하신 분?")

    if message.content == "콱봇 Tronix" or message.content == "콱봇 tronix" or message.content == "콱봇 트로닉스":
        counter("개발자에 대해 출력합니다.")
        await client.send_message(message.channel, "저를 만든 사람이라고 하네요!")

    if message.content == "콱봇 Rio" or message.content == "콱봇 rio" or message.content == "콱봇 리오":
        counter("Rio에 대해 출력합니다.")
        await client.send_message(message.channel, "제 친구 기어봇의 개발자입니다!")

    if message.content == "콱봇 굴굴이":
        counter("굴굴이에 대해 출력합니다.")
        await client.send_message(message.channel, "제 친구 근육돼지의 개발자입니다!")

    if message.content == "콱봇 오리":
        counter("Rio에 대해 반대로 출력합니다.")
        await client.send_message(message.channel, "!다니입자발개 의봇킹띵 구친 제")

    if message.content == "콱봇 기어봇":
        counter("기어봇에 대해 출력합니다.")
        await client.send_message(message.channel, "제 친구이자 제 개발자의 친구의 봇입니다!")

    # if "지뢰봇" in message.content:
    #     counter("지뢰봇에 대해 출력합니다.")
    #     await client.send_message(message.channel, "그 친구는 죽었다구요...ㅠㅠ")

    if message.content == "콱봇 근육돼지":
        await client.send_message(message.channel, "그 친구는 항상 먹고 있더라고요!")

        # 엔터테인먼트
    if message.content == "콱봇 사로" or message.content == "콱봇 saro":
        counter("Saro의 동영상을 보여줍니다.")
        saro1 = "WBC 챔피언 Saro의 **WBC Elimination** 영상입니다!\n" \
                "https://www.youtube.com/watch?v=CqmqBpZlzKQ"
        saro2 = "GBBB 챔피언 Saro의 **GBBB 모음집**입니다!\n" \
                "https://www.youtube.com/watch?v=mhA-FeUrQJg"
        saro3 = "Saro의 대표곡인 **ORAS**입니다!\n" \
                "https://www.youtube.com/watch?v=bEIBm7H-E98"
        saro4 = "Saro의 곡 중 하나인 **PIEGE**입니다!\n" \
                "https://www.youtube.com/watch?v=mYGYh62Sgpo"
        saro = random.choice([saro1, saro2, saro3, saro4])
        await client.send_message(message.channel, saro)

        # 실용적인 기능
        # 선택
    if message.content.startswith("콱봇 선택") or message.content.startswith("콱봇 골라"):
        try:
            counter("콱봇이 항목들 중 하나를 선택합니다.")
            choose_input = message.content.split(" ", 2)
            choose = choose_input[2].split()
        except IndexError:
            pass
        else:
            choose_result = random.choice(choose)
            choose_embed = discord.Embed(
                title="콱봇의 선택은...",
                description=choose_result,
                color=0xffff00
            )
            await client.send_message(message.channel, embed=choose_embed)

        # 번역
    if message.content.startswith("콱봇 한영번역"):
        counter("한국어에서 영어로 번역합니다.")

        text = message.content[8:]

        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers = {"X-Naver-Client-Id": "Fnvncjby_Lr5i3UgJRN2", "X-Naver-Client-Secret": "H_UIdPVHgm"}
        params = {"source": "ko", "target": "en", "text": text}

        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()

        trans_ke_embed = discord.Embed(
            title="한영 번역 결과입니다.",
            description=result["message"]["result"]["translatedText"],
            color=0x00ffff
        )
        await client.send_message(message.channel, embed=trans_ke_embed)

    if message.content.startswith("콱봇 영한번역"):
        counter("영어에서 한국어로 번역합니다.")

        text = message.content[8:]

        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers = {"X-Naver-Client-Id": "Fnvncjby_Lr5i3UgJRN2", "X-Naver-Client-Secret": "H_UIdPVHgm"}
        params = {"source": "en", "target": "ko", "text": text}

        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()

        trans_ek_embed = discord.Embed(
            title="영한 번역 결과입니다.",
            description=result["message"]["result"]["translatedText"],
            color=0x00ffff
        )
        await client.send_message(message.channel, embed=trans_ek_embed)

        # 시간
    if message.content == "콱봇 시간":
        counter("시간을 출력합니다.")
        now = datetime.now()
        time_embed = discord.Embed(
            title="현재 시간은...",
            description="**%d시 %d분 %d초**입니다!" % (abs(now.hour - 12), now.minute, now.second),
            color=0xffff00
        )
        await client.send_message(message.channel, embed=time_embed)

    if message.content == "콱봇 날짜":
        counter("날짜를 출력합니다.")
        now = datetime.now()
        date_embed = discord.Embed(
            title="오늘 날짜는...",
            description="**%d년 %d월 %d일**입니다!" % (now.year, now.month, now.day),
            color=0xffff00
        )
        await client.send_message(message.channel, embed=date_embed)

    if message.content == "콱봇 시간날짜":
        counter("시간과 날짜를 출력합니다.")
        now = datetime.now()
        timedate_embed = discord.Embed(
            title="지금은...",
            description="**%d년 %d월 %d일\n%d시 %d분 %d초**입니다!"
                        % (now.year, now.month, now.day, abs(now.hour - 12), now.minute, now.second),
            color=0xffff00
        )
        await client.send_message(message.channel, embed=timedate_embed)

        # 사이트 이동
    if message.content.startswith("콱봇 사이트"):
        counter("특정 사이트로 이동합니다.")
        try:
            site = message.content[7:]
        except IndexError:
            pass
        else:
            # site_embed 만드는 함수 생성
            def createSiteEmbed(site_name, site_url, site_thumbnail):
                SiteEmbed = discord.Embed(
                    title=site_name,
                    description="[사이트로 이동하기](%s)" % site_url,
                    color=0x00ffff
                )
                SiteEmbed.set_thumbnail(
                    url=site_thumbnail
                )
                return SiteEmbed

            if site == "네이버" or site == "naver":
                site_embed = createSiteEmbed("네이버", "https://www.naver.com/", "https://media.discordapp.net/attachments/554154900020396033/554291327181783062/mobile_212852414260.png")
                await client.send_message(message.channel, embed=site_embed)

            if site == "구글" or site == "google":
                site_embed = createSiteEmbed("Google", "https://www.google.com/", "https://media.discordapp.net/attachments/554154900020396033/554301508834033664/AAuE7mAOzJeUhnaCQpCrB8z58jvoroZFpAAB_9nD7ws900-mo-c-c0xffffffff-rj-k-no.png")
                await client.send_message(message.channel, embed=site_embed)

            if site == "다음" or site == "daum":
                site_embed = createSiteEmbed("다음", "https://www.daum.net/", "https://media.discordapp.net/attachments/554154900020396033/554295052411863050/5587C4E4012FCD0001.png")
                await client.send_message(message.channel, embed=site_embed)

            if site == "유튜브" or site == "youtube":
                site_embed = createSiteEmbed("YouTube", "https://www.youtube.com/", "https://media.discordapp.net/attachments/554154900020396033/554296606158094366/yt_1200-vfl4C3T0K.png")
                await client.send_message(message.channel, embed=site_embed)

            if site == "깃허브" or site == "github":
                site_embed = createSiteEmbed("GitHub", "https://www.github.com/", "https://cdn.discordapp.com/attachments/554154900020396033/554319935480922112/9919.png")
                await client.send_message(message.channel, embed=site_embed)

            if site == "사운드클라우드" or site == "soundcloud":
                site_embed = createSiteEmbed("SoundCloud", "https://soundcloud.com/discover", "https://cdn.discordapp.com/attachments/554154900020396033/554321777866702872/u4Xt7sb8_400x400.png")
                await client.send_message(message.channel, embed=site_embed)

            if site == "페이스북" or site == "facebook":
                site_embed = createSiteEmbed("Facebook", "https://www.facebook.com", "https://cdn.discordapp.com/attachments/554154900020396033/554322603763040270/fb_icon_325x325.png")
                await client.send_message(message.channel, embed=site_embed)

            if site == "해시코드" or site == "hashcode":
                site_embed = createSiteEmbed("Hashcode", "https://hashcode.co.kr/", "https://cdn.discordapp.com/attachments/554324092313141268/554325207968645133/ic_meta-d75a4fdc9eacdac15ab7d016ee69babf6aff049b1fc80a55f86dad5560da2cee.png")
                await client.send_message(message.channel, embed=site_embed)

    if message.content == "콱봇 사이트 목록":
        site_list_embed = discord.Embed(
            title="사이트 목록입니다.",
            description="네이버 naver\n"
            "구글 google\n"
            "다음 daum\n"
            "유튜브 youtube\n"
            "깃허브 github\n"
            "사운드클라우드 soundcloud\n"
            "페이스북 facebook\n"
            "해시코드 hashcode",
            color=0xffffff
        )
        await client.send_message(message.channel, embed=site_list_embed)

        # 콱봇과 놀기
        # 가위바위보
    if message.content.startswith("콱봇 가위바위보"):
        counter("콱봇과 가위바위보를 합니다.")

        await client.send_message(message.channel, "가위바위보 중에 고르세요!")
        gbb_user = await client.wait_for_message(timeout=5, author=message.author, channel=message.channel)

        if gbb_user is None:
            gbb_timeover_embed = discord.Embed(
                title="시간이 지났습니다.",
                description="왜 안 고르세요? :(",
                color=0xff0000
            )
            await client.send_message(message.channel, embed=gbb_timeover_embed)

        else:
            gbb_user = gbb_user.content
            gbb_list = ["가위", "바위", "보"]
            gbb_com = random.choice(gbb_list)

            if gbb_user not in gbb_list:
                gbb = "이상한 거 내지 말라구욧!"
            if (gbb_user == "가위" and gbb_com == "보") or (gbb_user == "바위" and gbb_com == "가위") or (gbb_user == "보" and gbb_com == "바위"):
                gbb = "<@%s>님이 이겼네요! 축하해요~" % message.author.id
            if (gbb_user == "가위" and gbb_com == "바위") or (gbb_user == "바위" and gbb_com == "보") or (gbb_user == "보" and gbb_com == "가위"):
                gbb = "<@%s>님이 졌네요..." % message.author.id
            if gbb_user == gbb_com:
                gbb = "비겼네요. ㅎㅎ"

            gbb_embed = discord.Embed(
                title="콱봇의 선택 : %s" % gbb_com,
                description=gbb,
                color=0xffff00
            )
            await client.send_message(message.channel, embed=gbb_embed)

        # 하나빼기
    if message.content.startswith("콱봇 하나빼기"):
        counter("콱봇과 하나빼기를 합니다.")

        await client.send_message(message.channel, "일단 먼저 가위바위보 중에 2개를 골라주세요! (공백 구분)")
        hnp_user_input = await client.wait_for_message(timeout=5, author=message.author, channel=message.channel)

        if hnp_user_input is None:
            hnp_timeover_embed_middle = discord.Embed(
                title="시간이 지났습니다.",
                description="왜 안 고르세요? :(",
                color=0xff0000
            )
            client.send_message(message.channel, embed=hnp_timeover_embed_middle)

        else:
            hnp_user_input = hnp_user_input.content.split()
            hnp_user1, hnp_user2 = hnp_user_input[0], hnp_user_input[1]
            hnp_list = ["가위", "바위", "보"]
            hnp_com1, hnp_com2 = 0, 0
            while hnp_com1 == hnp_com2:
                hnp_com1, hnp_com2 = random.choice(hnp_list), random.choice(hnp_list)

            hnp_embed_middle = discord.Embed(
                title="%s와 %s 중에 무엇을 내시겠어요?" % (hnp_user1, hnp_user2),
                description="콱봇 : %s  %s\n당신 : %s  %s" % (hnp_com1, hnp_com2, hnp_user1, hnp_user2)
            )
            await client.send_message(message.channel, embed=hnp_embed_middle)

            hnp_user = await client.wait_for_message(timeout=5, author=message.author, channel=message.channel)

            if hnp_user is None:
                hnp_timeover_embed = discord.Embed(
                    title="시간이 지났습니다.",
                    description="왜 안 고르세요? :(",
                    color=0xff0000
                )
                await client.send_message(message.channel, embed=hnp_timeover_embed)
            else:
                hnp_user = hnp_user.content
                hnp_com = random.choice([hnp_com1, hnp_com2])

                if hnp_user not in hnp_list:
                    hnp = "이상한 거 내지 말라구욧!"
                if (hnp_user == "가위" and hnp_com == "보") or (hnp_user == "바위" and hnp_com == "가위") or (hnp_user == "보" and hnp_com == "바위"):
                    hnp = "<@%s>님이 이겼네요! 축하해요~" % message.author.id
                if (hnp_user == "가위" and hnp_com == "바위") or (hnp_user == "바위" and hnp_com == "보") or (hnp_user == "보" and hnp_com == "가위"):
                    hnp = "<@%s>님이 졌네요..." % message.author.id
                if hnp_user == hnp_com:
                    hnp = "비겼네요. ㅎㅎ"

                hnp_embed = discord.Embed(
                    title="콱봇의 선택 : %s" % hnp_com,
                    description=hnp,
                    color=0xffff00
                )
                await client.send_message(message.channel, embed=hnp_embed)

    #     # 묵찌빠
    # if message.content == "콱봇 묵찌빠":
    #     counter("콱봇과 묵찌빠를 합니다.")
    #
    #     while True:
    #         await client.send_message(message.channel, "묵찌빠 중 하나를 골라주세요!")
    #         mjb_user = await client.wait_for_message(timeout=5, author=message.author, channel=message.channel)
    #
    #         if mjb_user is None:
    #             mjb_timeover_embed = discord.Embed(
    #                 title="시간이 지났습니다.",
    #                 description="왜 안 고르세요? :(",
    #                 color=0xff0000
    #             )
    #             client.send_message(message.channel, embed=mjb_timeover_embed)
    #
    #         else:
    #             mjb_attack, mjb_user_, mjb_count, mjb_attack, mjb = 0, 0, 0, 0, 0
    #
    #             def whattosay(cnt, old, new):  # title
    #                 if cnt == 0:
    #                     return "가위바위보!"
    #                 else:
    #                     return old + old + new + "!"
    #
    #             mjb_user = mjb_user.content
    #             mjb_list = ["묵", "찌", "빠"]
    #             mjb_com = random.choice(mjb_list)
    #
    #             mjb_middle_embed = discord.Embed(
    #                 title=whattosay(mjb_count, mjb_user_, mjb_user) + " 무엇을 내시겠어요?",
    #                 description="컴퓨터 : %s\n당신    : %s" % (mjb_com, mjb_user)
    #             )
    #             await client.send_message(message.channel, embed=mjb_middle_embed)
    #
    #             # 같은 것을 냈을 때
    #             if mjb_user == mjb_com:
    #                 if mjb_attack == "user":
    #                     mjb = "<@%s>님이 이겼네요! 축하해요~" % message.author.id
    #                     break
    #                 elif mjb_attack == "com":
    #                     mjb = "<@s>님이 졌네요..." % message.author.id
    #                     break
    #                 else:
    #                     mjb = "비겼습니다. 다시 해 주세요."
    #
    #             # 다른 것을 냈을 때
    #             else:
    #                 mjb_count += 1
    #
    #                 if (mjb_user == "묵" and mjb_com == "찌") or (mjb_user == "찌" and mjb_com == "빠") or (mjb_user == "빠" and mjb_com == "묵"):
    #                     mjb = "<@s>님이 이겼으므로 공격권을 가지게 되었습니다!" % message.author.id
    #                     mjb_attack = "user"
    #
    #                 else:
    #                     mjb = "컴퓨터가 이겼으므로 공격권을 뺏겼습니다!"
    #                     mjb_attack = "com"
    #
    #     mjb_embed = discord.Embed(
    #         title=mjb
    #     )
    #     await client.send_message(message.channel, embed=mjb_embed)





    if message.content == "콱봇 테스트":
        test_msg = await client.send_message(message.channel, "좋아요 싫어요")
        await client.add_reaction(test_msg, "👍")
        await client.add_reaction(test_msg, "👎")

        def check(reaction, user):
            e = str(reaction.emoji)
            return e.startswith(("👍", "👎"))
        test_res = await client.wait_for_reaction(message=test_msg, check=check, user=message.author)
        await client.send_message(message.channel, "{0.user} (이)가 {0.reaction.emoji} 로 응답했습니다!".format(test_res))

        # 기타
    if message.content == "콱봇 프사":
        counter("프로필 사진을 출력합니다.")
        bot_picture = "https://cdn.discordapp.com/attachments/547642671460515841/550260106751639554/awesome_face.png"
        await client.send_message(message.channel, "제 사진이에요!\n%s" % bot_picture)

client.run(token)
