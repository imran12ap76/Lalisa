class script(object):
    START_TXT = """๐๐ถ ๐ ๐ฎ๐๐ฒ,๐ฅฐ ๐ก๐ถ๐ฐ๐ฒ ๐ง๐ผ ๐ ๐ฒ๐ฒ๐ ๐ฌ๐ผ๐ {},
๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด ๐ธ๐ <a href=https://t.me/{}>{}</a>,
๐ ๐๐บ ๐ ๐ฆ๐ถ๐บ๐ฝ๐น๐ฒ ๐๐๐๐ผ ๐๐ถ๐น๐๐ฒ๐ฟ ๐๐ผ๐ ๐ช, 
๐ธ ๐ฒ๐ฐ๐ฝ ๐ฟ๐๐พ๐๐ธ๐ณ๐ด ๐ผ๐พ๐๐ธ๐ด๐,๐ฌ๐ฝ๏ธ ๐น๐๐๐ ๐ฐ๐ณ๐ณ ๐ผ๐ด ๐๐พ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐ฐ๐ฝ๐ณ ๐ด๐ฝ๐น๐พ๐ ๐
โ ๏ธ๐ฌ๐๐๐พ ๐ง๐พ๐๐ ๐ง๐๐ /help
๐ ๐ ๐ ๐๐ฟ๐ฒ๐ฎ๐๐ผ๐ฟ @Mhd_Imrann"""
    HELP_TXT = """<i>๐๐ปโโ๏ธ   ๐ง๐พ๐๐๐๐๐  {} ๐ค
โ  ๐๐'๐ ๐ญ๐๐๐พ ๐ข๐๐๐๐๐๐ผ๐บ๐๐พ๐ฝ...๐ค
โ  ๐ฒ๐พ๐บ๐๐ผ๐ ๐๐๐๐๐ ๐๐๐๐๐๐พ ๐๐๐ฝ๐พ...โญ
๐ณ๐๐๐ ๐๐พ๐๐๐๐ฝ ๐๐๐๐๐ ๐๐ ๐บ๐๐ ๐ผ๐๐บ๐, ๐ฉ๐๐๐ ๐๐๐๐พ <b>Bot Username</b> ๐บ๐๐ฝ ๐๐๐พ๐ ๐๐พ๐บ๐๐พ ๐บ ๐๐๐บ๐ผ๐พ ๐บ๐๐ฝ ๐๐พ๐บ๐๐ผ๐ ๐บ๐๐ ๐๐๐๐๐พ ๐๐๐ ๐๐บ๐๐..."""
    ABOUT_TXT = """<b>๐ฅฑ My Name : {}
๐ตโโ Dแดแด แดสแดแดแดส: <a href='https://t.me/Mhd_Imrann'>โ แชiฦฦแง แชลณษฌฦษงษเฝ โ</a>
๐ Lษชสสแดสส: <a href='https://docs.pyrogram.org/'>Pสสแดษขสแดแด</a>
๐ฅ Lแดษดษขแดแดษขแด: <a href='https://www.python.org/download/releases/3.0/'>Pสแดสแดษด 3</a>
๐ช DแดแดแดBแดsแด : <a href='https://www.mongodb.com/'>MแดษดษขแดDB</a>
๐ Bแดแดษขสแดแดแด : @PocketMoviesOfficial </b>"""
    SOURCE_TXT = """<b>NOTE:</b>
<b>โ ๏ธแดสษช๊ฑ สแดแด ษช๊ฑ ษดแดแด แดษด  แดแดแดษด ๊ฑแดแดสแดแด แดสแดแดแดแดแด
โ ๊ฑแดแดสแดแด แดแดแดแด : ๐ญ๐ฎ๐ณ ๐ ๐ต๐ ๐จ๐ซ๐ ๐ก๐ซ๐ค ๐ฑ๐จ๐ฆ๐ง๐ณ ๐ญ๐ฎ๐ถ
โ แดแดแดแด ๊ฐษชสแดแดส : <a href=https://github.com/sathanxavier1998/autofilterctv5>[๐๐โข]๐๐ฎ๐ญ๐จ๐๐ข๐ฅ๐ญ๐๐ซ๐๐จ๐ญV3</a>
โ สแดแด แด ๊ฐสแดแด :  <a href=https://t.me/PocketMoviesOfficial>Tamilrockersโข</a>
โ Qแดแดสษชแด๊ฑ : <a href=https://t.me/Mhd_Imrann>King</a></b>"""
    MANUELFILTER_TXT = """สแดสแด: <b>๊ฐษชสแดแดส๊ฑ</b>
- ๊ฐษชสแดแดส ษช๊ฑ แด ๊ฐแดแดแดแดสแด แดกแดสแด แด๊ฑแดส๊ฑ แดแดษด ๊ฑแดแด แดแดแดแดแดแดแดแดแด สแดแดสษชแด๊ฑ ๊ฐแดส แด แดแดสแดษชแดแดสแดส แดแดสแดกแดสแด แดษดแด ษช แดกษชสส สแด๊ฑแดแดษดแด แดกสแดษดแดแด แดส แด แดแดสแดกแดสแด ษช๊ฑ ๊ฐแดแดษดแด ษชษด แดสแด แดแด๊ฑ๊ฑแดษขแด

<b>ษดแดแดแด:</b>
1.๐ แดสษช๊ฑ สแดแด ๊ฑสแดแดสแด สแดแด แด แดแดแดษชษด แดสษชแด ษชสแดษขแด.
2.๐ แดษดสส แดแดแดษชษด๊ฑ แดแดษด แดแดแด ๊ฐษชสแดแดส๊ฑ ษชษด แด แดสแดแด.
3.๐แดสแดสแด สแดแดแดแดษด๊ฑ สแดแด แด แด สษชแดษชแด แด๊ฐ 64 แดสแดสแดแดแดแดส๊ฑ.

Cแดแดแดแดษดแดs Aษดแด Usแดษขแด:
โข /filter - <code>แดแดแด แด ๊ฐษชสแดแดส ษชษด แด แดสแดแด โพ๏ธ</code>
โข /filters - <code>สษช๊ฑแด แดสส แดสแด ๊ฐษชสแดแดส๊ฑ แด๊ฐ แด แดสแดแดโพ๏ธ</code>
โข /del - <code>แดแดสแดแดแด แด ๊ฑแดแดแดษช๊ฐษชแด ๊ฐษชสแดแดส ษชษด แด แดสแดแดโพ๏ธ</code>
โข /delall - <code>แดแดสแดแดแด แดสแด แดกสแดสแด ๊ฐษชสแดแดส๊ฑ ษชษด แด แดสแดแด (แดสแดแด แดแดกษดแดส แดษดสส)โพ๏ธ</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
ษช แดแดษด ๊ฑแดแดแดแดสแด สแดแดส แดสส แดษดแด แดสแดสแด ษชษดสษชษดแด สแดแดแดแดษด๊ฑ ๐ฌ๐ช

<b>NOTE:</b>
1. แดแดสแดษขสแดแด แดกษชสส ษดแดแด แดสสแดแดก๊ฑ สแดแด แดแด ๊ฑแดษดแด สแดแดแดแดษด๊ฑ แดกษชแดสแดแดแด แดษดส แดแดษดแดแดษดแด, ๊ฑแด แดแดษดแดแดษดแด ษช๊ฑ แดแดษดแดแดแดแดสส.
2. แดสษช๊ฑ สแดแด ๊ฑแดแดแดแดสแด๊ฑ สแดแดแดแดษด๊ฑ แดกษชแดส แดษดส แดแดสแดษขสแดแด แดแดแดษชแด แดสแดแด.
3. สแดแดแดแดษด๊ฑ ๊ฑสแดแดสแด สแด แดสแดแดแดสสส แดแดส๊ฑแดแด แด๊ฑ แดแดสแดแดแดแดกษด ๊ฐแดสแดแดแด

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Autofiltersathan_V2_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """สแดสแด: <b>แดแดแดแด ๊ฐษชสแดแดส</b>
<b>ษดแดแดแด: Fษชสแด Iษดแดแดx</b>
1. แดแดแดแด แดแด แดสแด แดแดแดษชษด แด๊ฐ สแดแดส แดสแดษดษดแดส ษช๊ฐ ษชแด'๊ฑ แดสษชแด แดแดแด.
2. แดแดแดแด ๊ฑแดสแด แดสแดแด สแดแดส แดสแดษดษดแดส แดแดแด๊ฑ ษดแดแด แดแดษดแดแดษชษด๊ฑ แดแดแดสษชแด๊ฑ, แดแดสษด แดษดแด ๊ฐแดแดแด ๊ฐษชสแด๊ฑ.
3. ๊ฐแดสแดกแดสแด แดสแด สแด๊ฑแด แดแด๊ฑ๊ฑแดษขแด แดแด แดแด แดกษชแดส Qแดแดแดแด๊ฑ. ษช'สส แดแดแด แดสส แดสแด ๊ฐษชสแด๊ฑ ษชษด แดสแดแด แดสแดษดษดแดส แดแด แดส แดส.

<b>Nแดแดแด: AแดแดแดFษชสแดแดส</b>
1. Aแดแด แดสแด สแดแด แดs แดแดแดษชษด แดษด สแดแดส ษขสแดแดแด.
2. Usแด /connect แดษดแด แดแดษดษดแดแดแด สแดแดส ษขสแดแดแด แดแด แดสแด สแดแด.
3. Usแด /settings แดษด สแดแด's PM แดษดแด แดแดสษด แดษด AแดแดแดFษชสแดแดส แดษด แดสแด sแดแดแดษชษดษขs แดแดษดแด."""
    CONNECTION_TXT = """สแดสแด: <b>แดแดษดษดแดแดแดษชแดษด๊ฑ</b>
- แด๊ฑแดแด แดแด แดแดษดษดแดแดแด สแดแด แดแด แดแด ๊ฐแดส แดแดษดแดษขษชษดษข ๊ฐษชสแดแดส๊ฑ 
- ษชแด สแดสแด๊ฑ แดแด แดแด แดษชแด ๊ฑแดแดแดแดษชษดษข ษชษด ษขสแดแดแด๊ฑ.
<b>ษดแดแดแด:</b>

1. แดษดสส แดแดแดษชษด๊ฑ แดแดษด แดแดแด แด แดแดษดษดแดแดแดษชแดษด.
2. ๊ฑแดษดแด <code>/แดแดษดษดแดแดแด</code> ๊ฐแดส แดแดษดษดแดแดแดษชษดษข แดแด แดแด สแดแดส แดแด

Cแดแดแดแดษดแดs Aษดแด Usแดษขแด:
โข /connect  - <code>แดแดษดษดแดแดแด แด แดแดสแดษชแดแดสแดส แดสแดแด แดแด สแดแดส แดแด</code>
โข /disconnect  - <code>แดษช๊ฑแดแดษดษดแดแดแด ๊ฐสแดแด แด แดสแดแด</code>
โข /connections - <code>สษช๊ฑแด แดสส สแดแดส แดแดษดษดแดแดแดษชแดษด๊ฑ</code>"""
    EXTRAMOD_TXT = """สแดสแด: Exแดสแด Mแดแดแดสแดs
<b>ษดแดแดแด:</b>

๐นแดสแด๊ฑแด แดสแด แดสแด แดxแดสแด ๊ฐแดแดแดแดสแด๊ฑ แด๊ฐ แดสษช๊ฑ สแดแด

Cแดแดแดแดษดแดs Aษดแด Usแดษขแด:
โข /id - <code>ษขแดแด ษชแด แด๊ฐ แด ๊ฑแดแดแดษช๊ฐษชแดแด แด๊ฑแดส.</code>
โข /info  - <code>ษขแดแด ษชษด๊ฐแดสแดแดแดษชแดษด แดสแดแดแด แด แด๊ฑแดส.</code>
โข /imdb  - <code>ษขแดแด แดสแด ๊ฐษชสแด ษชษด๊ฐแดสแดแดแดษชแดษด ๊ฐสแดแด ษชแดแดส ๊ฑแดแดสแดแด.</code>
โข /search  - <code>ษขแดแด แดสแด ๊ฐษชสแด ษชษด๊ฐแดสแดแดแดษชแดษด ๊ฐสแดแด แด แดสษชแดแด๊ฑ ๊ฑแดแดสแดแด๊ฑ.</code>"""
    ADMIN_TXT = """สแดสแด: Aแดแดษชษด Mแดแดs
<b>ษดแดแดแด:</b>
Tสษชs Mแดแดแดสแด Oษดสส Wแดสแดs Fแดส Mส Aแดแดษชษดs
Cแดแดแดแดษดแดs Aษดแด Usแดษขแด:
โข /logs - <code>แดแด ษขแดแด แดสแด สแดแดแดษดแด แดสสแดส๊ฑ</code>
โข /stats - <code>แดแด ษขแดแด ๊ฑแดแดแดแด๊ฑ แด๊ฐ ๊ฐษชสแด๊ฑ ษชษด แดส. [Tสษชs Cแดแดแดแดษดแด Cแดษด Bแด Usแดแด Bส Aษดสแดษดแด]</code>
โข /delete - <code>แดแด แดแดสแดแดแด แด ๊ฑแดแดแดษช๊ฐษชแด ๊ฐษชสแด ๊ฐสแดแด แดส.</code>
โข /users - <code>แดแด ษขแดแด สษช๊ฑแด แด๊ฐ แดส แด๊ฑแดส๊ฑ แดษดแด ษชแด๊ฑ.</code>
โข /chats - <code>แดแด ษขแดแด สษช๊ฑแด แด๊ฐ แดส แดสแดแด๊ฑ แดษดแด ษชแด๊ฑ</code>
โข /leave  - <code>แดแด สแดแดแด แด ๊ฐสแดแด แด แดสแดแด.</code>
โข /disable  -  <code>แดแด แดษช๊ฑแดสสแด แด แดสแดแด.</code>
โข /ban  - <code>แดแด สแดษด แด แด๊ฑแดส.</code>
โข /unban  - <code>แดแด แดษดสแดษด แด แด๊ฑแดส.</code>
โข /channel - <code>แดแด ษขแดแด สษช๊ฑแด แด๊ฐ แดแดแดแดส แดแดษดษดแดแดแดแดแด แดสแดษดษดแดส๊ฑ</code>
โข /broadcast - <code>แดแด สสแดแดแดแดแด๊ฑแด แด แดแด๊ฑ๊ฑแดษขแด แดแด แดสส แด๊ฑแดส๊ฑ</code>"""
    

    STATUS_TXT = """<b>๐ แดแดแดแดส าษชสแดs: <code>{}</code>
๐ค แดแดแดแดส แดsแดสs: <code>{}</code>
โป๏ธ แดแดแดแดส แดสแดแดs: <code>{}</code>
๐๏ธ แดsแดแด sแดแดสแดษขแด: <code>{}</code>
๐ าสแดแด sแดแดสแดษขแด: <code>{}</code></b>"""
    
    LOG_TEXT_G = """#NewGroup
Gสแดแดแด = {}(<code>{}</code>)
Tแดแดแดส Mแดแดสแดสs = <code>{}</code>
Aแดแดแดแด Bส - {}"""
    
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nแดแดแด - {}"""
    
