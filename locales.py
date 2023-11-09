from locales_dict import Locale, LocalesDict

locale_pt = Locale()  #  Portuguese
locale_en = Locale()  #  English
locale_ru = Locale()  #  Russian
locale_uk = Locale()  #  Ukrainian
locale_de = Locale()  #  German
locale_it = Locale()  #  Italian
locale_fr = Locale()  #  French	 
locale_es = Locale()  #  Spanish
locale_ja = Locale()  #  Japanese 
locale_zh = Locale()  #  Chinese  
locale_hi = Locale()  #  Hindi    
locale_ar = Locale()  #  Arabic 

locales = LocalesDict({
    'pt': locale_pt,
    'en': locale_en,
    'ru': locale_ru,
    'uk': locale_uk,
    'de': locale_de,
    'it': locale_it,
    'fr': locale_fr,
    'es': locale_es,
    'ja': locale_ja,
    'zh': locale_zh,
    'hi': locale_hi,
    'ar': locale_ar
}, locale_en)

# TOO_LONG_TITLE
locale_pt.too_long_title = '😮 Sua mensagem é muito longa'
locale_en.too_long_title = '😮 Your message is too long'
locale_ru.too_long_title = '😮 Слишком длинное сообщение'
locale_uk.too_long_title = '😮 Занадто довге повідомлення'
locale_de.too_long_title = '😮 Deine Nachricht ist zu lang'
locale_it.too_long_title = '😮 Il tuo messaggio è troppo lungo'
locale_de.too_long_title = '😮 Deine Nachricht ist zu lang'
locale_fr.too_long_title = '😮 Votre message est trop long'
locale_es.too_long_title = '😮 Tu mensaje es demasiado largo'
locale_ja.too_long_title = '😮 メッセージが長すぎます'
locale_zh.too_long_title = '😮 你的信息太長了'
locale_hi.too_long_title = '😮 आपका संदेश बहुत लंबा है'
locale_ar.too_long_title = '😮 رسالتك طويلة جدًا'

# FOR_TITLE
locale_pt.for_title = '💬 Enviar mensagem para  %s'
locale_en.for_title = '💬 For %s'
locale_ru.for_title = '💬 Для %s'
locale_uk.for_title = '💬 Для %s'
locale_de.for_title = '💬 Für %s'
locale_it.for_title = '💬 Per %s'
locale_fr.for_title = '💬 Pour %s'
locale_es.for_title = '💬 Para %s'
locale_ja.for_title = '💬 %s へ'
locale_zh.for_title = '💬 发送消息给 %s'
locale_hi.for_title = '💬 Untuk %s'
locale_ar.for_title = '💬 برای %s'

# EXCEPT_TITLE
locale_pt.except_title = '💬 Enviar mensagem para para todos, menos %s'
locale_en.except_title = '💬 Except %s'
locale_ru.except_title = '💬 Кроме %s'
locale_uk.except_title = '💬 Крім %s'
locale_de.except_title = '💬 Akzeptiere %s'
locale_it.except_title = '💬 Tranne %s'
locale_fr.except_title = '💬 Sauf %s'
locale_es.except_title = '💬 Excepto %s'
locale_ja.except_title = '💬 %s を除く'
locale_zh.except_title = '💬 除了 %s'
locale_hi.except_title = '💬 %s को छोड़कर'
locale_ar.except_title = '💬 باستثناء %s'

# SPOILER_TITLE
locale_pt.spoiler_title = '✅ Revelar mensagem para todos'    
locale_en.spoiler_title = '✅ Spoiler'
locale_ru.spoiler_title = '✅ Спойлер'
locale_uk.spoiler_title = '✅ Спойлер'
locale_de.spoiler_title = '✅ Spoiler'
locale_it.spoiler_title = '✅ Spoiler'
locale_fr.spoiler_title = '✅ Spoiler'
locale_es.spoiler_title = '✅ Spoiler'
locale_ja.spoiler_title = '✅ スポイラー'
locale_zh.spoiler_title = '✅ 劇透'
locale_hi.spoiler_title = '✅ स्पॉइलर'
locale_ar.spoiler_title = '✅ سبويلر'

# TOO_LONG_MESSAGE
locale_pt.too_long_message = '🥺 Desculpe, sua mensagem não pode ser enviada porque excedeu o limite de 200 caracteres.'
locale_en.too_long_message = '🥺 Sorry, your message can\'t be sent as it exceeds the limit of 200 characters.'
locale_ru.too_long_message = '🥺 Ваше сообщение не может быть отправлено, так как его длина превышает лимит в 200 символов.'
locale_uk.too_long_message = '🥺 Ваше повідомлення не може бути відправлено, так як його довжина перевищує ліміт в 200 символів.'
locale_de.too_long_message = '🥺 Sorry, deine Nachricht kann nicht gesendet werden, da sie das Limit von 200 Zeichen überschreitet.'
locale_it.too_long_message = '🥺 Mi dispiace, il tuo messaggio non può essere mandato, supera il limite di 200 caratteri.'
locale_fr.too_long_message = '🥺 Désolé, votre message ne peut pas être envoyé car il dépasse la limite de 200 caractères.'
locale_es.too_long_message = '🥺 Lo siento, tu mensaje no puede ser enviado ya que excede el límite de 200 caracteres.'
locale_ja.too_long_message = '🥺 200文字の制限を超えたため、メッセージを送信できません。'
locale_zh.too_long_message = '🥺 对不起，您的消息无法发送，因为它超过了200个字符的限制。'
locale_hi.too_long_message = '🥺 क्षमा करें, आपका संदेश 200 अक्षरों की सीमा से अधिक होने के कारण भेजा नहीं जा सकता है।'
locale_ar.too_long_message = '🥺 عذرا، لا يمكن إرسال رسالتك لأنها تتجاوز الحد المسموح به من 200 حرف.'

# FOR_MESSAGE
locale_pt.for_message = '🔒 Mensagem secreta enviada com sucesso para %s.'
locale_en.for_message = '🔒 Private message for %s.'
locale_ru.for_message = '🔒 Приватное сообщение для %s.'
locale_uk.for_message = '🔒 Приватне повідомлення для %s.'
locale_de.for_message = '🔒 Private Nachricht für %s.'
locale_it.for_message = '🔒 Messaggio privato per %s.'
locale_fr.for_message = '🔒 Message privé pour %s.'
locale_es.for_message = '🔒 Mensaje privado para %s.'
locale_ja.for_message = '🔒 %s へのプライベート メッセージ。'
locale_zh.for_message = '🔒 給 %s 的私信。'
locale_hi.for_message = '🔒 %s के लिए निजी संदेश।'
locale_ar.for_message = '🔒 رسالة خاصة ل %s.'

# EXCEPT_MESSAGE
locale_pt.except_message = '💬 %s, você foi excluído(a) desta mensagem secreta.'
locale_en.except_message = '💬 Private message for everyone except %s.'
locale_ru.except_message = '💬 Приватное сообщение для всех, кроме %s.'
locale_uk.except_message = '💬 Приватне повідомлення для всіх, крім %s.'
locale_de.except_message = '💬 Private Nachricht an alle außer %s.'
locale_it.except_message = '💬 Messaggio privato per tutti tranne %s.'
locale_fr.except_message = '💬 Message privé pour tout le monde sauf %s.'
locale_es.except_message = '💬 Mensaje privado para todos excepto %s.'
locale_ja.except_message = '💬 %s以外の全員へのプライベートメッセージ。'
locale_zh.except_message = '💬 给除%s之外的所有人的私人消息。'
locale_hi.except_message = '💬 %s को छोड़कर सभी के लिए निजी संदेश।'
locale_ar.except_message = '💬 رسالة خاصة للجميع ما عدا %s.'


# SPOILER_MESSAGE
locale_pt.spoiler_message = '👥 Mensagem enviada para todos os integrantes do grupo.'
locale_en.spoiler_message = '👥 Public spoiler message.'
locale_ru.spoiler_message = '👥 Публичное сообщение под спойлером.'
locale_uk.spoiler_message = '👥 Публічне повідомлення під спойлером.'
locale_de.spoiler_message = '👥 Öffentlicher Spoiler für alle:'
locale_it.spoiler_message = '👥 Messaggio contenente spoiler.'
locale_fr.spoiler_message = '👥 Spoiler public.'
locale_es.spoiler_message = '👥 Spoiler público.'
locale_ja.spoiler_message = '👥 パブリックスポイラーメッセージ。'
locale_zh.spoiler_message = '👥 公共剧透消息。'
locale_hi.spoiler_message = '👥 सार्वजनिक स्पॉइलर संदेश।'
locale_ar.spoiler_message = '👥 رسالة حرق للجميع.'


# GROUP_GREETING_MESSAGE
locale_pt.group_greeting_message = (
         '👋 Olá, meu nome é %s! Obrigado por me adicionar em seu grupo\n\n'
         '🗺️ Posso ajudá-lo a enviar mensagens privadas que apenas os usuarios escolhidos por você podem ver.\n\n'
         '🔱 Para saber mais envie /start@%s e sinta-se à vontade para pedir ajuda em nosso '
         '<a href="t.me/pombomsgbotchannel">Canal oficial</a> e <a href="t.me/kylorensbot">Suporte</a> se você tiver alguma dúvida.')
locale_en.group_greeting_message = (
         '👋 Hello, my name is %s! Thanks for adding me to your group\n\n'
         '🗺️ I can help you send private messages that only the users you choose can see.\n\n'
         '🔱 To learn more send /start@%s and feel free to ask for help on our '
         '<a href="t.me/pombomsgbotchannel">Official channel</a> and <a href="t.me/kylorensbot">Support</a> if you have any questions.')
locale_ru.group_greeting_message = (
          '👋 Привет, меня зовут %s! Спасибо, что добавили меня в свою группу\n\n'
          '🗺️ Я могу помочь вам отправлять личные сообщения, которые могут видеть только выбранные вами пользователи.\n\n'
          '🔱 Чтобы узнать больше, отправьте /start@%s и не стесняйтесь обращаться за помощью в нашу '
          '<a href="t.me/pombomsgbotchannel">Официальный канал</a> и <a href="t.me/kylorensbot">Поддержка</a>, если у вас есть какие-либо вопросы.')
locale_uk.group_greeting_message = (
          '👋 Привіт, мене звати %s! Дякую за додавання мене до вашої групи\n\n'
          '🗺️ Я можу допомогти вам надсилати приватні повідомлення, які можуть бачити тільки користувачі, яких ви виберете.\n\n'
          '🔱 Щоб дізнатися більше, відправте /start@%s та не соромтеся звертатися за допомогою до нашого '
          '<a href="t.me/pombomsgbotchannel">Офіційного каналу</a> та <a href="t.me/kylorensbot">Підтримки</a>, якщо у вас є якісь питання.')
locale_de.group_greeting_message = (
          '👋 Hallo, mein Name ist %s! Danke, dass du mich zu deiner Gruppe hinzugefügt hast\n\n'
          '🗺️ Ich kann dir helfen, private Nachrichten zu senden, die nur die von dir ausgewählten Benutzer sehen können.\n\n'
          '🔱 Um mehr zu erfahren, senden Sie /start@%s und fragen Sie auf unserer '
          '<a href="t.me/pombomsgbotchannel">Offizieller Kanal</a> und <a href="t.me/kylorensbot">Support</a>, wenn Sie Fragen haben.')
locale_it.group_greeting_message = (
          '👋 Ciao, mi chiamo %s! Grazie per avermi aggiunto al tuo gruppo\n\n'
          '🗺️ Posso aiutarti a inviare messaggi privati che solo gli utenti che scegli possono vedere.\n\n'
          '🔱 Per saperne di più invia /start@%s e sentiti libero di chiedere aiuto sul nostro '
          '<a href="t.me/pombomsgbotchannel">Canale ufficiale</a> e <a href="t.me/kylorensbot">Assistenza</a> in caso di domande.')
locale_fr.group_greeting_message = (
          '👋 Bonjour, je m\'appelle %s! Merci de m\'avoir ajouté à votre groupe\n\n'
          '🗺️ Je peux vous aider à envoyer des messages privés que seuls les utilisateurs que vous choisissez peuvent voir.\n\n'
          '🔱 Pour en savoir plus, envoyez /start@%s et n\'hésitez pas à demander de l\'aide sur notre '
          '<a href="t.me/pombomsgbotchannel">Chaîne officielle</a> et <a href="t.me/kylorensbot">Assistance</a> si vous avez des questions.')
locale_es.group_greeting_message = (
          '👋 ¡Hola, mi nombre es %s! Gracias por agregarme a tu grupo\n\n'
          '🗺️ Puedo ayudarte a enviar mensajes privados que solo pueden ver los usuarios que elijas.\n\n'
          '🔱 Para obtener más información, envíe /start@%s y no dude en solicitar ayuda en nuestro '
          '<a href="t.me/pombomsgbotchannel">Canal oficial</a> y <a href="t.me/kylorensbot">Soporte</a> si tiene alguna pregunta.')
locale_ja.group_greeting_message = (
          '👋 こんにちは、私の名前は%sです！グループに追加していただきありがとうございます\n\n'
          '🗺️ あなたが選んだユーザーだけが見ることができるプライベートメッセージを送信するのを手伝うことができます。\n\n'
          '🔱 もっと詳しく知りたい場合は、/start@%s を送信して、質問がある場合は '
          '<a href="t.me/pombomsgbotchannel">公式チャンネル</a>と<a href="t.me/kylorensbot">サポート</a>にお問い合わせください。')
locale_zh.group_greeting_message = (
         '👋 你好，我的名字是%s！感谢将我添加到你的群组中\n\n'
         '🗺️ 我可以帮助你发送仅有你选择的用户可以看到的私人消息\n\n'
         '🔱 要了解更多，请发送 /start@%s，并随时在我们的 '
         '<a href="t.me/pombomsgbotchannel">官方频道</a>和<a href="t.me/kylorensbot">支持</a>上寻求帮助，如果您有任何问题。')
locale_hi.group_greeting_message = (
          '👋 नमस्ते, मेरा नाम %s है! आपके समूह में जोड़ने के लिए धन्यवाद\n\n'
          '🗺️ मैं आपको उन निश्चित उपयोगकर्ताओं तक निजी संदेश भेजने में मदद कर सकता हूँ, जो आप चुनते हैं।\n\n'
          '🔱 और अधिक जानने के लिए /start@%s भेजें और अगर आपके पास कोई सवाल हो तो हमारे '
          '<a href="t.me/pombomsgbotchannel">आधिकारिक चैनल</a> और <a href="t.me/kylorensbot">सहायता</a> पर मदद के लिए पूछने में स्वतंत्र महसूस करें। ')
locale_ar.group_greeting_message = (
         '👋 مرحبًا ، اسمي %s! شكرًا على إضافتي إلى مجموعتك\n\n'
         '🗺️ يمكنني مساعدتك في إرسال رسائل خاصة يمكن للمستخدمين الذين تختارهم فقط رؤيتها.\n\n'
         '🔱 للمزيد من المعلومات ، أرسل /start@%s ولا تتردد في طلب المساعدة على '
         '<a href="t.me/pombomsgbotchannel">القناة الرسمية</a> و <a href="t.me/kylorensbot">الدعم</a> إذا كان لديك أي أسئلة.')

# INFO_MESSAGE
locale_pt.info_message = (
        '@pombomsgbot é um bot inline do Telegram para <b>manter suas mensagens privadas escondidas de olhares indiscretos.</b>\n\n'
        'Envie mensagens privadas para um ou mais usuários no grupo, e tenha conversas privadas sem precisar ir no chat privado.\n\n'
        'Clique nos botões abaixo e entre nosso canal oficial com explicações e atualizações, o se preferir me chame através do suporte.\n\n'
        '👥<b>Canal de figurinhas:</b> <a href="https://t.me/lbrabo">Clique aqui</a>\n')
locale_en.info_message = (
         '@pombomsgbot is an inline Telegram bot to <b>keep your private messages hidden from prying eyes.</b>\n\n'
         'Send private messages to one or more users in the group, and have private conversations without having to go to private chat.\n\n'
         'Click on the buttons below and enter our official channel with explanations and updates, or if you prefer, call me through support.\n\n'
         '👥 <b>Sticker channel:</b> <a href="https://t.me/lbrabo">Click here</a>\n')
locale_ru.info_message = (
         '@pombomsgbot — это встроенный бот Telegram, <b>который скрывает ваши личные сообщения от посторонних глаз.</b>\n\n'
         'Отправляйте личные сообщения одному или нескольким пользователям в группе и ведите личные беседы, не переходя в приватный чат.\n\n'
         'Нажмите на кнопки ниже и войдите в наш официальный канал с объяснениями и обновлениями, или, если хотите, позвоните мне через службу поддержки.\n\n'
         '👥 <b>Канал стикеров:</b> <a href="https://t.me/lbrabo">Нажмите здесь</a>\n')
locale_uk.info_message = (
         '@pombomsgbot — вбудований бот Telegram, який <b>приховує ваші особисті повідомлення від сторонніх очей.</b>\n\n'
         'Надсилайте приватні повідомлення одному чи кільком користувачам у групі та ведіть приватні розмови без необхідності переходити в приватний чат.\n\n'
         'Натисніть кнопки нижче та перейдіть на наш офіційний канал із поясненнями та оновленнями або, якщо хочете, зателефонуйте мені через службу підтримки.\n\n'
         '👥 <b>Канал наклейок:</b> <a href="https://t.me/lbrabo">Натисніть тут</a>\n')
locale_de.info_message = (
         '@pombomsgbot ist ein Inline-Telegram-Bot, um <b>Ihre privaten Nachrichten vor neugierigen Blicken zu verbergen.</b>\n\n'
         'Private Nachrichten an einen oder mehrere Benutzer in der Gruppe senden und private Unterhaltungen führen, ohne in den privaten Chat gehen zu müssen.\n\n'
         'Klicken Sie auf die Schaltflächen unten und betreten Sie unseren offiziellen Kanal mit Erklärungen und Updates, oder rufen Sie mich über den Support an, wenn Sie dies vorziehen.\n\n'
         '👥 <b>Stickerkanal:</b> <a href="https://t.me/lbrabo">Klicken Sie hier</a>\n')
locale_it.info_message = (
          '@pombomsgbot è un bot di Telegram integrato <b>per mantenere i tuoi messaggi privati nascosti da occhi indiscreti.</b>\n\n'
          'Invia messaggi privati a uno o più utenti del gruppo e conversa in privato senza dover accedere alla chat privata.\n\n'
          'Fai clic sui pulsanti in basso ed entra nel nostro canale ufficiale con spiegazioni e aggiornamenti, o se preferisci chiamami tramite il supporto.\n\n'
          '👥 <b>Canale adesivi:</b> <a href="https://t.me/lbrabo">Clicca qui</a>\n')
locale_fr.info_message = (
          '@pombomsgbot est un bot Telegram en ligne <b>pour garder vos messages privés cachés des regards indiscrets.</b>\n\n'
          'Envoyer des messages privés à un ou plusieurs utilisateurs du groupe et avoir des conversations privées sans avoir à accéder au chat privé.\n\n'
          'Cliquez sur les boutons ci-dessous et accédez à notre chaîne officielle avec des explications et des mises à jour, ou si vous préférez, appelez-moi via l\'assistance.\n\n'
          '👥 <b>Chaîne d\'autocollants :</b> <a href="https://t.me/lbrabo">Cliquez ici</a>\n')
locale_es.info_message = (
          '@pombomsgbot es un bot de Telegram en línea para <b>mantener tus mensajes privados ocultos de miradas indiscretas.</b>\n\n'
          'Envía mensajes privados a uno o más usuarios del grupo y mantén conversaciones privadas sin tener que ir al chat privado.\n\n'
          'Haz clic en los botones de abajo e ingresa a nuestro canal oficial con explicaciones y actualizaciones, o si lo prefieres, llámame a través de soporte.\n\n'
          '👥 <b>Canal de pegatinas:</b> <a href="https://t.me/lbrabo">Haz clic aquí</a>\n')
locale_ja.info_message = (
          '@pombomsgbot は、プライベート <b>メッセージを覗き見されないようにするためのインライン テレグラム ボットです。</b>\n\n'
          'グループ内の 1 人以上のユーザーにプライベート メッセージを送信し、プライベート チャットに行かなくてもプライベートな会話ができます。\n\n'
          '下のボタンをクリックして、説明と最新情報が記載された公式チャンネルにアクセスしてください。または、必要に応じて、サポートを通じて私に電話してください。\n\n'
          '👥 <b>ステッカー チャンネル:</b> <a href="https://t.me/lbrabo">ここをクリックしてください</a>\n')
locale_zh.info_message = (
          '@pombomsgbot 是一個內嵌的 Telegram <b>機器人，可以保護您的私人消息不被窺視。</b>\n\n'
          '向群組中的一位或多位用戶發送私人消息，無需進入私人聊天即可進行私人對話。\n\n'
          '單擊下面的按鈕並進入我們的官方頻道，其中包含解釋和更新，或者如果您願意，請通過支持給我打電話。\n\n'
          '👥 <b>貼紙頻道：</b> <a href="https://t.me/lbrabo">点击这里</a>\n')
locale_hi.info_message = (
          '@pombomsgbot आपके निजी संदेशों <b>को ताक-झांक करने वाली नज़रों से छुपाने के लिए एक इनलाइन टेलीग्राम बॉट है।</b>\n\n'
          'समूह में एक या अधिक उपयोगकर्ताओं को निजी संदेश भेजें, और निजी चैट पर जाए बिना निजी वार्तालाप करें।\n\n'
          'नीचे दिए गए बटनों पर क्लिक करें और स्पष्टीकरण और अपडेट के साथ हमारे आधिकारिक चैनल में प्रवेश करें, या यदि आप चाहें, तो मुझे समर्थन के माध्यम से कॉल करें।\n\n'
          '👥<b> स्टिकर चैनल:</b> <a href="https://t.me/lbrabo">यहाँ क्लिक करें</a>\n')
locale_ar.info_message = (
          '@pombomsgbot هو روبوت Telegram <b>مضمّن لإخفاء رسائلك الخاصة عن أعين المتطفلين. </b>\n\n'
          'أرسل رسائل خاصة إلى مستخدم واحد أو أكثر في المجموعة ، واستمتع بمحادثات خاصة دون الحاجة إلى الذهاب إلى محادثة خاصة. \n\n'
          'انقر فوق الأزرار أدناه وادخل إلى قناتنا الرسمية مع الشروحات والتحديثات ، أو اتصل بي من خلال الدعم ، إذا كنت تفضل ذلك. \n\n'
          '👥 <b>قناة الملصق:</b> <a href="https://t.me/lbrabo">انقر هنا</a>\n')

# HOW_TO_USE
locale_pt.how_to_use = 'Como usar este bot?'
locale_en.how_to_use = 'How to use this bot?'
locale_ru.how_to_use = 'Как пользоваться этим ботом?'
locale_uk.how_to_use = 'Як користуватися цим ботом?'
locale_de.how_to_use = 'Wie geht das?'
locale_it.how_to_use = 'Come usare questo bot?'
locale_fr.how_to_use = 'Comment utiliser ce bot ?'
locale_es.how_to_use = '¿Cómo usar este bot?'
locale_ja.how_to_use = 'このボットの使い方'
locale_zh.how_to_use = '如何使用此机器人？'
locale_hi.how_to_use = 'इस बॉट का उपयोग कैसे करें?'
locale_ar.how_to_use = 'كيفية استخدام هذا الروبوت؟'


# TOO_LONG_DESCRIPTION
locale_pt.too_long_description = 'Reduza o tamanho da sua mensagem para que não exceda o limite de 200 caracteres.🤏'
locale_en.too_long_description = 'Please shorten the length of your message so that it doesn\'t exceed the limit of 200 characters.🤏'
locale_ru.too_long_description = 'Пожалуйста, сократите длину вашего сообщения, чтобы она не превышала лимит в 200 символов.🤏'
locale_uk.too_long_description = 'Будь ласка, скоротіть довжину Вашого повідомлення, щоб вона не перевищувала ліміт в 200 символів.🤏'
locale_de.too_long_description = 'Bitte fasse dich etwas kürzer und überschreite das Limit von 200 Zeichen nicht.🤏'
locale_it.too_long_description = 'Perfavore accorcia la lunghezza del tuo messaggio in modo che non superi i 200 caratteri.🤏'
locale_fr.too_long_description = 'Veuillez raccourcir la longueur de votre message pour qu\'il ne dépasse pas la limite de 200 caractères.🤏'
locale_es.too_long_description = 'Por favor, acorte la longitud de su mensaje para que no exceda el límite de 200 caracteres.🤏'
locale_ja.too_long_description = 'メッセージの長さが200文字を超えないように、メッセージを短くしてください。🤏'
locale_zh.too_long_description = '请缩短消息的长度，以使其不超过200个字符的限制。🤏'
locale_hi.too_long_description = 'कृपया अपना संदेश इतना छोटा करें कि यह 200 अक्षर की सीमा से अधिक न हो।🤏'
locale_ar.too_long_description = 'يرجى تقصير طول رسالتك حتى لا يتجاوز الحد الأقصى للـ 200 حرف.🤏'


# NOT_ALLOWED
locale_pt.not_allowed = 'Você não tem permissão para visualizar este conteúdo.🔐'
locale_en.not_allowed = 'You are not allowed to view this content.🔐'
locale_ru.not_allowed = 'Вам запрещено просматривать этот контент.🔐'
locale_uk.not_allowed = 'Вам заборонено переглядати цей контент.🔐'
locale_de.not_allowed = 'Dir ist nicht gestattet, diesen Inhalt zu lesen.🔐'
locale_it.not_allowed = 'Non hai il permesso per vedere questo messaggio.🔐'
locale_fr.not_allowed = 'Vous n\'êtes pas autorisé à voir ce contenu.🔐'
locale_es.not_allowed = 'No tienes permitido ver este contenido.🔐'
locale_ja.not_allowed = 'このコンテンツを表示することは許可されていません。🔐'
locale_zh.not_allowed = '您无权查看此内容。🔐'
locale_hi.not_allowed = 'आप इस सामग्री को देखने की अनुमति नहीं हैं।🔐'
locale_ar.not_allowed = 'لا يُسمح لك بعرض هذا المحتوى.🔐'

# NOT_ACCESSIBLE
locale_pt.not_accessible = 'Este conteúdo não está mais acessível.🚫'
locale_en.not_accessible = 'This content is no longer accessible.🚫'
locale_ru.not_accessible = 'Этот контент больше недоступен.🚫'
locale_uk.not_accessible = 'Цей контент більше недоступний.🚫'
locale_de.not_accessible = 'Der Inhalt ist nicht mehr sichtbar.🚫'
locale_it.not_accessible = 'Questo contenuto non è più accessibile.🚫'
locale_fr.not_accessible = 'Ce contenu n\'est plus accessible.🚫'
locale_es.not_accessible = 'Este contenido ya no está disponible.🚫'
locale_ja.not_accessible = 'このコンテンツはもうアクセスできません。🚫'
locale_zh.not_accessible = '此内容不再可访问。🚫'
locale_hi.not_accessible = 'यह सामग्री अब अधिक उपलब्ध नहीं है।🚫'
locale_ar.not_accessible = 'لا يمكن الوصول إلى هذا المحتوى بعد الآن.🚫'


# VIEW
locale_pt.view = 'ᴄʟɪǫᴜᴇ ᴘᴀʀᴀ ʟᴇʀ 🔓'
locale_en.view = 'View 🔓'
locale_ru.view = 'Открыть 🔓'
locale_uk.view = 'Відкрити 🔓'
locale_de.view = 'Ansehen 🔓'
locale_it.view = 'Vedi 🔓'
locale_fr.view = 'Voir 🔓'
locale_es.view = 'Ver 🔓'
locale_ja.view = '表示 🔓'
locale_zh.view = '查看 🔓'
locale_hi.view = 'देखें 🔓'
locale_ar.view = 'عرض 🔓'


# AND_CONNECTOR
locale_pt.and_connector = 'ᴇ'
locale_en.and_connector = 'and'
locale_ru.and_connector = 'и'
locale_uk.and_connector = 'i'
locale_de.and_connector = '&'
locale_it.and_connector = 'e'
locale_fr.and_connector = 'et'
locale_es.and_connector = 'y'
locale_ja.and_connector = 'と'
locale_zh.and_connector = '和'
locale_hi.and_connector = 'और'
locale_ar.and_connector = 'و'


# Add Group
locale_pt.button_addGroup = '✨ Adicione-me em seu grupo'
locale_en.button_addGroup = '✨ Add me to your group'
locale_ru.button_addGroup = '✨ Добавьте меня в вашу группу'
locale_uk.button_addGroup = '✨ Додайте мене до вашої групи'
locale_de.button_addGroup = '✨ Füge mich zu deiner Gruppe hinzu'
locale_it.button_addGroup = '✨ Aggiungimi al tuo gruppo'
locale_fr.button_addGroup = '✨ Ajoutez-moi à votre groupe'
locale_es.button_addGroup = '✨ Añádeme a tu grupo'
locale_ja.button_addGroup = '✨ グループに私を追加してください'
locale_zh.button_addGroup = '✨ 把我加入你的群组中'
locale_hi.button_addGroup = '✨ मुझे अपने समूह में जोड़ें'
locale_ar.button_addGroup = '✨ أضفني إلى مجموعتك'

# Channel
locale_pt.button_channel_message = '📢 Canal Oficial'
locale_en.button_channel_message = '📢 Official Channel'
locale_ru.button_channel_message = '📢 Официальный канал'
locale_uk.button_channel_message = '📢 Офіційний канал'
locale_de.button_channel_message = '📢 Offizieller Kanal'
locale_it.button_channel_message = '📢 Canale ufficiale'
locale_fr.button_channel_message = '📢 Chaîne officielle'
locale_es.button_channel_message = '📢 Canal oficial'
locale_ja.button_channel_message = '📢 公式チャンネル'
locale_zh.button_channel_message = '📢 官方频道'
locale_hi.button_channel_message = '📢 आधिकारिक चैनल'
locale_ar.button_channel_message = '📢 القناة الرسمية'

# Donate
locale_pt.button_donate_message = '🤝 Doação'
locale_en.button_donate_message = '🤝 Donation'
locale_ru.button_donate_message = '🤝 Пожертвование'
locale_uk.button_donate_message = '🤝 Пожертвування'
locale_de.button_donate_message = '🤝 Spende'
locale_it.button_donate_message = '🤝 Donazione'
locale_fr.button_donate_message = '🤝 Don'
locale_es.button_donate_message = '🤝 Donación'
locale_ja.button_donate_message = '🤝 寄付'
locale_zh.button_donate_message = '🤝 捐款'
locale_hi.button_donate_message = '🤝 दान'
locale_ar.button_donate_message = '🤝 هبة'

# Use
locale_pt.button_use_message = '❓ Como usar'
locale_en.button_use_message = '❓ How to use'
locale_ru.button_use_message = '❓ Как использовать'
locale_uk.button_use_message = '❓ Як користуватися'
locale_de.button_use_message = '❓ Anwendung'
locale_it.button_use_message = '❓ Come usare'
locale_fr.button_use_message = '❓ Comment utiliser'
locale_es.button_use_message = '❓ Cómo usar'
locale_ja.button_use_message = '❓ 使い方'
locale_zh.button_use_message = '❓ 如何使用'
locale_hi.button_use_message = '❓ कैसे उपयोग करें'
locale_ar.button_use_message = '❓ كيفية الاستخدام'

# Support
locale_pt.button_support_message = '👨‍💻 Suporte'
locale_en.button_support_message = '👨‍💻 Support'
locale_ru.button_support_message = '👨‍💻 Поддержка'
locale_uk.button_support_message = '👨‍💻 Підтримка'
locale_de.button_support_message = '👨‍💻 Unterstützung'
locale_it.button_support_message = '👨‍💻 Supporto'
locale_fr.button_support_message = '👨‍💻 Support'
locale_es.button_support_message = '👨‍💻 Soporte'
locale_ja.button_support_message = '👨‍💻 サポート'
locale_zh.button_support_message = '👨‍💻 支持'
locale_hi.button_support_message = '👨‍💻 समर्थन'
locale_ar.button_support_message = '👨‍💻 الدعم'

# Command Start
locale_pt.commands_start = 'Menu inicial'
locale_en.commands_start = 'Home Menu'
locale_ru.commands_start = 'Главное меню'
locale_uk.commands_start = 'Головне меню'
locale_de.commands_start = 'Startmenü'
locale_it.commands_start = 'Menu principale'
locale_fr.commands_start = 'Menu principal'
locale_es.commands_start = 'Menú principal'
locale_ja.commands_start = 'ホームメニュー'
locale_zh.commands_start = '主菜单'
locale_hi.commands_start = 'मुख्य मेनू'
locale_ar.commands_start = 'القائمة الرئيسية'

# Command Help
locale_pt.commands_help = 'Como usar o bot'
locale_en.commands_help = 'How to use the bot'
locale_ru.commands_help = 'Как использовать бота'
locale_uk.commands_help = 'Як використовувати бота'
locale_de.commands_help = 'Wie man den Bot verwendet'
locale_it.commands_help = 'Come utilizzare il bot'
locale_fr.commands_help = 'Comment utiliser le bot'
locale_es.commands_help = 'Cómo usar el bot'
locale_ja.commands_help = 'ボットの使用方法'
locale_zh.commands_help = '如何使用机器人'
locale_hi.commands_help = 'बॉट का उपयोग कैसे करें'
locale_ar.commands_help = 'كيفية استخدام البوت'

# Short description
locale_pt.short_description = 'É um bot embutido para manter suas mensagens privadas escondidas. \n\nCanal Oficial: @pombomsgbotchannel'
locale_en.short_description = 'Is an inline bot to keep your private messages hidden. \n\nOfficial Channel: @pombomsgbotchannel'
locale_ru.short_description = 'Бот для скрытия ваших личных сообщений от ненавязчивых глаз. \n\nОфициальный канал: @pombomsgbotchannel'
locale_uk.short_description = 'Бот для приховування ваших особистих повідомлень від нав\'язливих очей. \n\nОфіційний канал: @pombomsgbotchannel'
locale_de.short_description = 'Ein integrierter Bot zum Ausblenden Ihrer privaten Nachrichten. \n\nOffizieller Kanal: @pombomsgbotchannel'
locale_it.short_description = 'È un bot integrato per nascondere i tuoi messaggi privati. \n\nCanale ufficiale: @pombomsgbotchannel'
locale_fr.short_description = 'Est un robot en ligne pour protéger vos messages privés. \n\nChaîne officielle : @pombomsgbotchannel'
locale_es.short_description = 'Es un bot en línea para ocultar tus mensajes privados de miradas curiosas. \n\nCanal oficial: @pombomsgbotchannel'
locale_ja.short_description = 'このインラインボットは、あなたのプライベートメッセージを他人の目から隠すためのものです。 \n\n公式チャンネル：@pombomsgbotchannel'
locale_zh.short_description = '这是一个内联机器人，用于保护您的私人消息不受窥探。 \n\n官方频道：@pombomsgbotchannel'
locale_hi.short_description = 'यह एक इंलाइन बॉट है जिसका उपयोग आपके निजी संदेशों को चुपा सकते हैं। \n\nआधिकृत चैनल: @pombomsgbotchannel'
locale_ar.short_description = 'هذا هو بوت مضمن لإخفاء رسائلك الخاصة عن الأعين الفضولية. \n\nالقناة الرسمية: @pombomsgbotchannel'

# description
locale_pt.description = 'A função do bot é enviar mensagens privadas para uma ou mais pessoas do grupo que você deseja. Não lemos a sua mensagem, privacidade e confiabilidade é o nosso lema. Canal Oficial: @pombomsgbotchannel'
locale_en.description = 'The bot\'s function is to send private messages to one or more people in the group that you want. We don\'t read your message, privacy and reliability is our motto. Official Channel: @pombomsgbotchannel'
locale_ru.description = 'Функция бота - отправлять личные сообщения одному или нескольким людям в группе, которую вы хотите. Мы не читаем ваше сообщение, конфиденциальность и надежность - наш девиз. Официальный канал: @pombomsgbotchannel'
locale_uk.description = 'Функція бота - надсилати особисті повідомлення одній або декільком людям у групі, яку ви бажаєте. Ми не читаємо ваше повідомлення, конфіденційність та надійність - наш девіз. Офіційний канал: @pombomsgbotchannel'
locale_de.description = 'Die Funktion des Bots besteht darin, private Nachrichten an eine oder mehrere Personen in der Gruppe zu senden, die Sie möchten. Wir lesen Ihre Nachricht nicht, Privatsphäre und Zuverlässigkeit sind unser Motto. Offizieller Kanal: @pombomsgbotchannel'
locale_it.description = 'La funzione del bot è inviare messaggi privati a una o più persone nel gruppo che desideri. Non leggiamo il tuo messaggio, la privacy e la affidabilità sono il nostro motto. Canale ufficiale: @pombomsgbotchannel'
locale_fr.description = 'La fonction du bot est d\'envoyer des messages privés à une ou plusieurs personnes du groupe de votre choix. Nous ne lisons pas votre message, la confidentialité et la fiabilité sont notre devise. Chaîne officielle : @pombomsgbotchannel'
locale_es.description = 'La función del bot es enviar mensajes privados a una o más personas en el grupo que desees. No leemos tu mensaje, la privacidad y la confiabilidad son nuestro lema. Canal oficial: @pombomsgbotchannel'
locale_ja.description = 'このボットの機能は、希望するグループ内の1人以上の人々にプライベートメッセージを送信することです。私たちはあなたのメッセージを読みません、プライバシーと信頼性が私たちのモットーです。公式チャンネル：@pombomsgbotchannel'
locale_zh.description = '该机器人的功能是向您想要的群组中的一个或多个人发送私人消息。我们不会阅读您的消息，隐私和可靠性是我们的座右铭。官方频道：@pombomsgbotchannel'
locale_hi.description = 'बॉट का कार्य है कि आप चाहें तो समूह में एक या एक से अधिक व्यक्तियों को निजी संदेश भेजें। हम आपका संदेश नहीं पढ़ते, गोपनीयता और विश्वसनीयता हमारा मोटो है। आधिकृत चैनल: @pombomsgbotchannel'
locale_ar.description = 'وظيفة البوت هي إرسال رسائل خاصة إلى شخص واحد أو أكثر في المجموعة التي ترغب فيها. نحن لا نقرأ رسالتك، الخصوصية والموثوقية هما شعارنا. القناة الرسمية: @pombomsgbotchannel'

# Bot Name
locale_pt.bot_name = 'Pombo Correio'
locale_en.bot_name = 'Carrier Pigeon'
locale_ru.bot_name = 'Голубь-почтовик'
locale_uk.bot_name = 'Голуб-поштар'
locale_de.bot_name = 'Brieftaube'
locale_it.bot_name = 'Piccione postino'
locale_fr.bot_name = 'Pigeon voyageur'
locale_es.bot_name = 'Paloma mensajera'
locale_ja.bot_name = '運搬鳩'
locale_zh.bot_name = '信鸽'
locale_hi.bot_name = 'कैरियर पिजन'
locale_ar.bot_name = 'حمامة الحمل'

# HOW TO USE LINKS
locale_pt.how_to_use_link = 'https://telegra.ph/pombomsgbot-pt-11-05'
locale_en.how_to_use_link = 'https://telegra.ph/pombomsgbot-en-11-05'
locale_ru.how_to_use_link = 'https://telegra.ph/pombomsgbot-ru-11-05'
locale_uk.how_to_use_link = 'https://telegra.ph/pombomsgbot-uk-11-05'
locale_de.how_to_use_link = 'https://telegra.ph/pombomsgbot-de-11-05'
locale_it.how_to_use_link = 'https://telegra.ph/pombomsgbot-it-11-05'
locale_fr.how_to_use_link = 'https://telegra.ph/pombomsgbot-fr-11-05'
locale_es.how_to_use_link = 'https://telegra.ph/pombomsgbot-es-11-05'
locale_ja.how_to_use_link = 'https://telegra.ph/pombomsgbot-ja-11-05'
locale_zh.how_to_use_link = 'https://telegra.ph/pombomsgbot-zh-11-05'
locale_ar.how_to_use_link = 'https://telegra.ph/pombomsgbot-ar-11-05'
locale_hi.how_to_use_link = 'https://telegra.ph/pombomsgbot-hi-11-06'

