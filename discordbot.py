import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('ハスくん起動')
    mainchannel = client.get_channel('603445142560702466')
    await client.send_message(mainchannel, 'ハスくん起動　!amidaであみだするよ\n')

@client.event
async def on_message(message):
    if message.content.startswith('!amida'):
       await client.send_message(message.channel,"あみだするよ")
       vc = message.author.voice.voice_channel
       if vc:
          cmember = vc.voice_members
          print(cmember)
          random.shuffle(cmember)
          members = len(cmember)
          if members <= 1 :
             await client.send_message(message.channel,"2人以上が接続している状態で試してみて！")
          else:
             members = members // 2
             vcmember1 = cmember[:members]
             vcmember2 = cmember[members:]
             vcmember11 = ', '.join(map(str, vcmember1))
             vcmember22 = ', '.join(map(str, vcmember2))
             msg = discord.Embed(title='チーム分け結果',description="Aチーム：" + str(vcmember11) + "\n" + "Bチーム：" + str(vcmember22), colour=0x3498db)
             await client.send_message(message.channel,embed=msg)
        else:
            await client.send_message(message.channel,"vcに接続している状態で試してみて！！")
            
            
#''内にトークンを入れれば完成らしい
client.run(token)
