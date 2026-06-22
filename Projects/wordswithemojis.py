emoji_map_fun = {
    'happy':"😊",
    'love':"❤",
    'code':"⚓",
    "tea":"🤳",
    "sad":"😒"
}

updated_words = []

user_message = input('Enter your message')

for word in user_message.split():
    clean_word = word.lower().strip(".,!?")
    emoji = emoji_map_fun.get(clean_word,'')
    if emoji:
        updated_words.append(f' {word} {emoji} ')
    else:
        updated_words.append(word)

updated_message  = " ".join(updated_words)

print(updated_message)