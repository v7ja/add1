from pyrogram import Client,filters;from pyromod import listen;import time, asyncio

bh = Client("fake", 20223538, "4984257087b565cc0b1dafc7be4d23c4")

# للتجربة ارسل /add في المحفوظات.

@bh.on_message(filters.command("add"))
async def add(bh,msg):
	
	urj = await msg.chat.ask("ارسل معرف المجموعة الي تريد تاخذ منها :")
	kill = await msg.chat.ask("ارسل معرف محموعتك :")
	iio = kill.text
	user = await bh.get_chat(urj.text)
	try:
		await bh.join_chat(user.id)
	except:
		pass
	try:		
		gg = await bh.join_chat(iio)
	except:
		pass
	gg = await bh.get_chat(iio)
	g =  gg.id
	
	i = user.id
	Ss = 0
	Err=0
	mssg = await msg.reply("انتظر...")
	usr = []
	async for i_is in bh.get_chat_members(i,limit=45):
		if i_is.user.is_bot == True:
			pass
		else:
			try:
				await bh.add_chat_members(g, i_is.user.id)
			except:
				pass
	await msg.reply("تم الانتهاء.")
			
	
bh.run()
