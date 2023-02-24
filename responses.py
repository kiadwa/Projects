import random
def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == "hello" :
        return "Ho Ho! You are approaching me, instead of running away ?"

    if p_message == "who":
        return "KONO DIO DA!!!"

    if p_message == "za warudo":
        num = random.randint(1, 15)
        w = "MUDA"
        return str((num * (w + " "))+ "!!")

    if p_message == "!help":
        return "WRYYYYY!!"


