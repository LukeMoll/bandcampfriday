import datetime, random

greetings = ["Hi", "Howdy", "Ronlon", "Hey", "Wassup", "o/", "Eyup", "Hello", "Honlo", "Hey there"]
groups = ["y'all", "nerds", "folks", "humans", "eggs", "guys, gals, and nonbinary pals", "honksonk", "fellow beings", "friends", "all", "cool cats"]
emoji = ["😀","😃","😄","😁","🙂","😉","😊","😇","😍","🤩","😋","😛","🤑","🤗","🤭","😏","😮","😌","🤤","😵","‍","💫","🤯","🤠","😎","🤓","🧐","😮","😯","😲","😳","😤","😈","👻","👽","👾","🤖","😺","😸","😻","💥","🌞","⭐","🌟","🌠","🌈","🔥","✨","🎼","🎤","🎧","🎷","🎸","🎹","🎺","🎻","🥁","⏰","🎈","🎉","🎊","🎀","🎁","📯","🎙","️","🎚","️","🎛","️","📻","💻","🖥","️","🖨","️","⌨","️","🖱","️","🖲","️","💽","💿","📀","💡","💸","📈","📡","🗿"]
exclamations_pos = ["Nice", "Radical", "Yeet", "eep", "Pog", "Sick", "Hecc", "Noice", "Sweet", "Ayyyy", "\o/", "Swell", "Neat", "W00t", "Yay", "Great", "Brilliant", "Most splendiferous"]
exclamations_neg = ["Shucks", "Boo", "Fug", "Damn", "Aww", "Bruh", ":(", "Amazing", "Just wonderful", "Cree", "Opposite of nice"]

def get_message_yes(fri_end:datetime.datetime) -> str:
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    remaining = fri_end - now
    msg = ""

    msg += random.choice(greetings)
    msg += " "
    msg += random.choice(groups)
    msg += ", it's Bandcamp Friday"
    msg += "".join(random.choices(emoji, k=3))
    msg += "\n"
    msg += f"It will end in {remaining.total_seconds // 3600} hours and {(remaining.total_seconds // 60)%60} minutes\n"
    msg += random.choice(exclamations_pos)
    msg += "!"

    return msg

def get_message_no(fri_start:datetime.datetime) -> str:
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    until = fri_start - now
    msg = ""

    msg += random.choice(greetings)
    msg += " "
    msg += random.choice(groups)
    msg += ", it's not Bandcamp Friday yet."
    msg += "\n"
    msg += f"The next one is in {until.days} days.\n"
    msg += random.choice(exclamations_neg)
    msg += "!"

    return msg