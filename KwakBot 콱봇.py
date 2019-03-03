# client id : 547685961136603149
# token : NTQ3Njg1OTYxMTM2NjAzMTQ5.D06bTA.rqxzMYB8ErcwoMuwE1CP7THQ7kQ
# client secret : 63U9h5F9bVNXGkHXwk2LJCVCfioX6t1Y
# 노랑 : 0xffff00  청록 : 0x00ffff

import asyncio
import discord
import random
import requests
import json


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

        help_embed = discord.Embed(
            title="콱봇 도움말 :D",
            description="콱봇을 사용하는 방법에 대해서 설명합니다.",
            color=0xffffff
        )
        help_embed.add_field(
            name="도움말 보기",
            value="**콱봇 도와줘** or **콱봇 도움말** or **콱봇 help** : \n"
            "총 3가지의 방법으로 도움말을 불러오실 수 있습니다.",
            inline=False
        )
        help_embed.add_field(
            name="엔터테인먼트",
            value="**콱봇 사로** or **콱봇 saro** : "
            "루프스테이션의 신 Saro의 영상을 보실 수 있습니다.",
            inline=False
        )
        help_embed.add_field(
            name="선택하기",
            value="**콱봇 선택** a b c or **콱봇 골라** a b c: "
            "a, b, c 중 하나를 콱봇이 선택합니다.",
            inline=False
        )
        help_embed.add_field(
            name="번역하기",
            value="**콱봇 한영번역** 어쩌구저쩌구 : "
            "입력한 한국어를 영어로 번역합니다.\n"
            "**콱봇 영한번역** blahblah : "
            "입력한 영어를 한국어로 번역합니다.",
            inline=False
        )
        help_embed.add_field(
            name="콱봇과 놀기",
            value="**콱봇 가위바위보** : "
            "콱봇과 가위바위보를 합니다.\n"
            "**콱봇 하나빼기** : "
            "콱봇과 하나빼기를 합니다.\n"
            "**콱봇 묵찌빠** : "
            "만들기 귀찮습니다.",
            inline=False
        )
        help_embed.add_field(
            name="기타",
            value="**콱봇 프사** : "
            "콱봇의 프로필 사진을 보여줍니다."
        )
        help_embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/547642671460515841/551420106585145359/awesome_face.png"
        )
        help_embed.set_footer(
            text="by Tronix",
            icon_url="https://cdn.discordapp.com/attachments/547642671460515841/549600907700994050/KakaoTalk_20190127_152958900.jpg"
        )
        await client.send_message(message.channel, embed=help_embed)

    # 일상대화 (접두사(콱봇) 없음)
    if message.content == "콱봇":
        counter("콱봇이 대답합니다.")
        await client.send_message(message.channel, random.choice(["네?", "저 부르셨어요?", "왜요?"]))

    if message.content == "콱봇 안녕":
        counter("콱봇이 인사합니다.")
        await client.send_message(message.channel, "안녕하세요 :D")

    #     # 반응
    # if message.content.startswith("ㅋㅋㅋㅋㅋㅋ") or message.content.endswith("ㅋㅋㅋㅋㅋㅋ"):
    #     counter("콱봇이 따라 웃습니다.")
    #     await client.send_message(message.channel, "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

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

    #     # 욕 감지
    # words = ["씨발", "시발", "ㅅㅂ", "좆", "병신", "ㅄ", "ㅂㅅ", "쌍", "썅", "ㅆ", "개새끼", "새끼"]
    # for i in range(len(words)):
    #     if words[i] in message.content:
    #         counter("욕을 감지했습니다.")
    #         await client.delete_message(message)
    #         await client.send_message(message.channel, "<@%s>님 욕하지 마세요~~^^" % message.author.id)

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
        await client.send_message(message.channel, "제 친구 띵킹봇의 개발자입니다!")

    if message.content == "콱봇 굴굴이":
        counter("굴굴이에 대해 출력합니다.")
        await client.send_message(message.channel, "제 친구 근육돼지의 개발자입니다!")

    if message.content == "콱봇 오리":
        counter("Rio에 대해 반대로 출력합니다.")
        await client.send_message(message.channel, "!다니입자발개 의봇킹띵 구친 제")

    if message.content == "콱봇 띵킹봇":
        counter("띵킹봇에 대해 출력합니다.")
        await client.send_message(message.channel, "제 친구이자 제 개발자의 친구의 봇입니다!")

    if "지뢰봇" in message.content:
        counter("지뢰봇에 대해 출력합니다.")
        await client.send_message(message.channel, "그 친구는 죽었다구요...ㅠㅠ")

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

    if message.content == "콱봇 테스트":
        await client.send_message(message.channel, "아무거나 입력하세요.")
        await client.wait_for_message(timeout=10, author=message.author, channel=message.channel)
        msg = await client.send_message(message.channel, "아래 중 하나를 선택하세요.")
        await client.add_reaction(msg, "✊")
        await client.add_reaction(msg, "✌")
        await client.add_reaction(msg, "🖐")
        res = await client.wait_for_reaction(["✊", "✌", "🖐"], message=message, timeout=5, user=message.author)
        # await client.send_message(message.channel, res)
        print(res)




        # 기타
    if message.content == "콱봇 프사":
        counter("프로필 사진을 출력합니다.")
        bot_picture = "https://cdn.discordapp.com/attachments/547642671460515841/550260106751639554/awesome_face.png"
        await client.send_message(message.channel, "제 사진이에요!\n%s" % bot_picture)

client.run(token)
