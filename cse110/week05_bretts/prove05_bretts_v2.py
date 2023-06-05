import random
import os


# Text Wrap
def text_wrap(path_name):
    import textwrap
    wrapper = textwrap.TextWrapper(width=80)
    word_list = wrapper.wrap(text=path_name)
    for element in word_list:
        print(element)


# Intro
print()
fname = input('Your first name? ').title()
monster = input('Your favorite monster? ').lower()
print()
text_wrap(
    f"Find the happy ending. If things get intense, enter RESET or EXIT to bale. We are here for you, {fname}...always watching.")


# Game Content - Plan Outline
try_again = [f"Try again {fname}...", "What was that?...", "Say again...",
             "One more time...", f"Say what {fname}?...", "Which one...", "eh?..."]

path_list = [
    f"{fname}, your journey begins during a weekend cabin retreat, in the woods. Your friend had been asking for an overdue retreat from the city bustle for months. As you arrive late in the evening, the headlights outline a quaint log structure tucked back about 30 yards from the driveway. Still, a welcome site after a long drive up the dark mountain road. You tell her, you will be right back after you unlock the cabin door. About halfway to the door, your car lights shut off suddenly. Crickets stop chirping. Dead silence. Quickly you decide to either RUN to the cabin door, or calmly WALK BACK to the car.", "run", "walk back"]

path_1_list = [
    f"As you run to the cabin door, you unfold the note scribbled with the door lock code. Hastely you enter 9-9-9 and just like in the movies - the door does not open! As you lift your head in disbelief, you hear what sounds like slow and steady footsteps directly behind you. In a panic, you decide to either turn and FACE a possible {monster} or KICK down the door like the {fname}inator you think you are.", "face", "kick"]

path_1_1_list = [f"You slowly turn and face what looks like a dark {monster} with a long snout. You take a step back and yell STOP! The figure stops and lifts it's head, shrouded by a loose hood. It was just your friend in your oversized hoody! She asks what's wrong with the cabin door. You hand over the note and she laughs, a bit louder than expected. She said the note was upside down. The code was 6-6-6 silly. She was right, the door opened and we were finally safe and warm in the cabin. She asked if I could get our bags from the car as she was currently indisposed. Hhmm, I could either GET the BAGS now, or WAIT until the morning.", "get bags", "wait"]

path_1_1_1_list = [f"So off I ran back into the darkness down to the car. How silly it was thinking my friend was a {monster}. As I opened the trunk, I thought why did she pick this cabin so far from the city? She knew the door code, yet the code was only emailed to me. I lifted the bags, mine was packed full of new clothes and a laptop. Her bag seemed much heavier and bulkier than normal. Oh well, what could go wrong on a night, with a full moon breaking through the mist. I could either become a WEREWOLF and finally reveal to her my secret curse, or stay CALM and see what fun activities she has planned. Or maybe, I should use my supernatural full moon powers and turn back time to RESET my day.", "werewolf", "calm", "reset"]

path_2_list = ["You calmly walk back to the car, trying not to make any startling moves or sounds. Slowly open the car door and slide in like a ninja. You look around desperately only to find your friend is not there! Something is not right and you decide to man-up and look around outside. You get out your cell phone to use the small onboard flashlight. You thought, maybe try to CALL her cell phone first, or get out of the car and SEARCH for her in the dark woods.", "call", "search"]

path_2_2_list = [
    f"Quickly, you fat-finger dial your friend. Nothing. Then you notice you have zero cell reception. You realize how far away you are from the city, from people. No street lights, not even cabin lights are on. How can people live in such darkness - at night. Maybe a {monster}, but not me. Feels like the surrounding woods just swallow up light and anything that happens to walk into it. You decide to find your friend using your small phone flashlight. You either reach for a GUN you have hidden under your seat, or a loud WHISTLE you have in your glove box.", "gun", "whistle"]

path_2_2_2_list = ["You reach for the gun, but it is not there! You must have stored it in the trunk the last time you went to the shooting range. Slowly you slink out of the car and around back of the car. Only to see the trunk open and your startled friend quickly zipping up her bags. She said she was looking for a phone charger as her phone was out of battery. You forget about the gun and either give her a HUG, or SCOLD her for leaving the car. Or you are frustrated and want to EXIT this cabin locale pronto.", "hug", "scold", "exit"]

path_3_list = [
    f"You are done waiting. You must search and find her, before something else does. You quitely slide out of the car and use your tiny phone flashlight to scan the woods. It is like looking into a black hole. Nothing but black. Slowly you creep into the woods. The farther you go the less you see. You guessed it, your phone battery dies and now it is up to your enhanced senses. Listen, touch, step. Finally you find her curled up sleeping soundly by a large rock. You could hear her snoring and walk closer. As you try to wake her, the large rock moved. You have awkened the fabled {monster} of the black mountains. The {monster} roars and wants to either EAT you or RUN away.", "eat", "run"]

path_3_3_list = ["You step out of the car and blow your multistaged chambered high output lifeguard whistle. It was so loud, the entire forest was awake now. You can see many glowing eyes swaying back and forth in the woods. Some higher and larger than others. Then over by the wood pile, your friend calls for you to come over. She found a side entrance that was left open. Quickly you both go inside the cabin and relax. With the stress of evening gone, your friend wants to relax and either play CARDS or watch a MOVIE.", "cards", "movie"]

path_3_3_3_list = ["Cards are great way to chat and have fun at the same time you thought. Your friend slowly reaches behind her and pulls out a deck of worn out Tarot cards. She first reveals these cards were handed down to from generations past. We sit down on the carpet by the fireplace and she deals out my cards. She has you methodically turn over each card - explaining the meaning of each like she was reading her very own horoscope. On the last card she explains this one has a special meaning and should not be taken lightly. The card she turns over is either the PROSPER card, or the DEATH card.", "prosper", "death"]


# Path Choices
def path():
    print()
    text_wrap(path_list[0])
    while True:
        path_choice = input(
            f"What will you do - {path_list[1].upper()} or {path_list[2].upper()}? ").lower()
        if path_choice == "exit":
            break
        elif path_choice == "reset":
            os.system("cls")
            path()
            break
        elif path_choice == path_list[1]:
            path_1()
            break
        elif path_choice == path_list[2]:
            path_2()
            break
        elif path_choice != path_list[1] or path_choice != path_list[2]:
            print(random.choice(try_again))
        else:
            break


def path_1():
    print()
    text_wrap(path_1_list[0])
    while True:
        path_1_choice = input(
            f"What will you do - {path_1_list[1].upper()} or {path_1_list[2].upper()}? ").lower()
        if path_1_choice == "exit":
            break
        elif path_1_choice == "reset":
            os.system("cls")
            path()
            break
        elif path_1_choice == path_1_list[1]:
            path_1_1()
            break
        elif path_1_choice == path_1_list[2]:
            print()
            text_wrap(
                f"You kick the door open. Your patented {fname}inator Karate Super Kick! Only to have your friend yell at you for breaking the door and now you will have to pay the cabin owner to replace it. She was the one walking behind you...and is very annoyed. The next day she is in a bad mood and eventually breaks off your friendship. She can't be around someone that breaks doors as easily as her feelings. She calls you {monster}-breath and takes an Uber home. You leave alone with your tail between your legs.")
            print()
            break
        elif path_1_choice != path_1_list[1] or path_1_choice != path_1_list[2]:
            print(random.choice(try_again))
        else:
            break


def path_1_1():
    print()
    text_wrap(path_1_1_list[0])
    while True:
        path_1_1_choice = input(
            f"What will you do - {path_1_1_list[1].upper()} or {path_1_1_list[2].upper()}? ").lower()
        if path_1_1_choice == "exit":
            break
        elif path_1_1_choice == "reset":
            os.system("cls")
            path()
            break
        elif path_1_1_choice == path_1_1_list[1]:
            path_1_1_1()
            break
        elif path_1_1_choice == path_1_1_list[2]:
            print()
            text_wrap(
                f"You nicely ask to wait and unload the car tomorrow morning. You say we have so much to catch up on from being so busy and disconnected in the city. Best friends are hard to come by. She agrees and you both open up and share life stories and laugh. You did good {fname}. Your friendship has never been so strong. Eventually, you both fall asleep by the cozy fire. While you sleep, a spark pops out from the fireplace and burns the cabin down. You both die.")
            print()
            break
        elif path_1_1_choice != path_1_1_list[1] or path_1_1_choice != path_1_1_list[2]:
            print(random.choice(try_again))
        else:
            break


def path_1_1_1():
    print()
    text_wrap(path_1_1_1_list[0])
    while True:
        path_1_1_1_choice = input(
            f"What will you do - {path_1_1_1_list[1].upper()} or {path_1_1_1_list[2].upper()} or {path_1_1_1_list[3].upper()}? ").lower()
        if path_1_1_1_choice == "exit":
            break
        elif path_1_1_1_choice == "reset":
            os.system("cls")
            path()
            break
        elif path_1_1_1_choice == path_1_1_1_list[1]:
            print()
            text_wrap(
                f"{fname}, you can't control the beast inside you, and sadly, you kill her. Bad dog.")
            print()
            break
        elif path_1_1_1_choice == path_1_1_1_list[2]:
            print()
            text_wrap(
                "She eventually found out your secret, and brought all the weapons needed to kill a sleeping werewolf. You died.")
            print()
            break
        elif path_1_1_1_choice != path_1_1_1_list[1] or path_1_1_1_choice != path_1_1_1_list[2]:
            print(random.choice(try_again))
        else:
            break


def path_2():
    print()
    text_wrap(path_2_list[0])
    while True:
        path_2_choice = input(
            f"What will you do - {path_2_list[1].upper()} or {path_2_list[2].upper()}? ").lower()
        if path_2_choice == "exit":
            break
        elif path_2_choice == "reset":
            os.system("cls")
            path()
            break
        elif path_2_choice == path_2_list[1]:
            path_2_2()
            break
        elif path_2_choice == path_2_list[2]:
            path_3()
            break
        elif path_2_choice != path_2_list[1] or path_2_choice != path_2_list[2]:
            print(random.choice(try_again))
        else:
            break


def path_2_2():
    print()
    text_wrap(path_2_2_list[0])
    while True:
        path_2_2_choice = input(
            f"What will you do - {path_2_2_list[1].upper()} or {path_2_2_list[2].upper()}? ").lower()
        if path_2_2_choice == "exit":
            break
        elif path_2_2_choice == "reset":
            os.system("cls")
            path()
            break
        elif path_2_2_choice == path_2_2_list[1]:
            path_2_2_2()
            break
        elif path_2_2_choice == path_2_2_list[2]:
            path_3_3()
            break
        elif path_2_2_choice != path_2_2_list[1] or path_2_2_choice != path_2_2_list[2]:
            print(random.choice(try_again))
        else:
            break


def path_2_2_2():
    print()
    text_wrap(path_2_2_2_list[0])
    while True:
        path_2_2_2_choice = input(
            f"What will you do - {path_2_2_2_list[1].upper()} or {path_2_2_2_list[2].upper()} or {path_2_2_2_list[3].upper()}? ").lower()
        if path_2_2_2_choice == "exit":
            break
        elif path_2_2_2_choice == "reset":
            os.system("cls")
            path()
            break
        elif path_2_2_2_choice == path_2_2_2_list[1]:
            print()
            text_wrap(
                f"You try to give your friend a hug. Instead she pushes you away points what looks to be your own gun. She says, she knows you have been sneaking away some nights only to return sometimes covered in blood. You try to explain as a child you were bitten by a large {monster} and have been experiencing missing time. But she would have no more lies from {fname} and shoots you with a silver bullet. You die.")
            print()
            break
        elif path_2_2_2_choice == path_2_2_2_list[2]:
            print()
            text_wrap(
                f"You start yelling at your friend, talking how you could have been attacked by a {monster}. Who knows what lurks in these woods? The whole time she just smirked and did not say a word. You finally calm down and ask her if she understands you are worried for her safety. She stared a bit longer and revealed she had picked this cabin because it was her childhood home. Her Pa liked to take us kids out for nighly hunting trips in the woods. Confused, you ask what did you hunt at night? She replied with a large smile, anything that happens to walk in {fname}! She then attacks you just like a {monster} would - talk about irony. She sure was a cool friend at times, but also a vampire. You die.")
            print()
            break
        elif path_2_2_2_choice != path_2_2_2_list[1] or path_2_2_2_choice != path_2_2_2_list[2]:
            print(random.choice(try_again))
        else:
            break


def path_3():
    print()
    text_wrap(path_3_list[0])
    while True:
        path_3_choice = input(
            f"What will the {monster} do - {path_3_list[1].upper()} or {path_3_list[2].upper()}? ").lower()
        if path_3_choice == "exit":
            break
        elif path_3_choice == "reset":
            os.system("cls")
            path()
            break
        elif path_3_choice == path_3_list[1]:
            print()
            text_wrap(
                f"The {monster} eats you. A circle of life thing. You die.")
            print()
            break
        elif path_3_choice == path_3_list[2]:
            print()
            text_wrap(
                f"The {monster} runs away to it's mother that is also sleeping nearby. Mommy {monster} was not happy to see you bothering her child in the woods at night. You die {fname}...horribly. Words cannot explain how bad it was.")
            print()
            break
        elif path_3_choice != path_3_list[1] or path_3_choice != path_3_list[2]:
            print(random.choice(try_again))
        else:
            break


def path_3_3():
    print()
    text_wrap(path_3_3_list[0])
    while True:
        path_3_3_choice = input(
            f"What will you do - {path_3_3_list[1].upper()} or {path_3_3_list[2].upper()}? ").lower()
        if path_3_3_choice == "exit":
            break
        elif path_3_3_choice == "reset":
            os.system("cls")
            path()
            break
        elif path_3_3_choice == path_3_3_list[1]:
            path_3_3_3()
            break
        elif path_3_3_choice == path_3_3_list[2]:
            print()
            text_wrap(
                f"Your friend had already brought a movie in her purse. The Cabin in the Woods featuring {monster}s. She thought being in a cabin in the woods would make it even more scary than normal. She was right. The movie was so fear inducing that both of you stayed awake all night. And the next night. {fname}, you were so tired on the drive home you both fell asleep and drove off a cliff. You both died.")
            print()
            break
        elif path_3_3_choice != path_3_3_list[1] or path_3_3_choice != path_3_3_list[2]:
            print(random.choice(try_again))
        else:
            break


def path_3_3_3():
    print()
    text_wrap(path_3_3_3_list[0])
    while True:
        path_3_3_3_choice = input(
            f"What card will you be handed - {path_3_3_3_list[1].upper()} or {path_3_3_3_list[2].upper()}? ").lower()
        if path_3_3_3_choice == "exit":
            break
        elif path_3_3_3_choice == "reset":
            os.system("cls")
            path()
            break
        elif path_3_3_3_choice == path_3_3_3_list[1]:
            print()
            text_wrap(
                f"The Prosper Card, yes! Your friend was so happy for you. And you know what {fname}, she was on to something. The universe had chose you to be very prosperous. Stinking rich. After you came home from your cabin retreat, you created a pill that cures cancer overnight. You eventually married a celebrity. You owned most of Florida and even a {monster}. You had it all - so it seemed. As your wealth grew, so did the ambitions and greed of your own family. They contracted a mobster to show you how to sleep with the fishes. You died.")
            print()
            break
        elif path_3_3_3_choice == path_3_3_3_list[2]:
            print()
            text_wrap(
                f"As you flipped over the death card, your friend gasped. This could mean the end of life, she explained. However, it also can be the transition of life. Out with the old ways and in with the new. She explained most fear this card, they fear change. But her family has taught this can be the most powerful card in the deck. You have great things in store for you {fname}. She hugs you and we stay up chatting about life, future goals, even about {monster}s into the wee hours. You are surprised how much we have in common. The next couple of days brought you both even closer as friends. With each cabin sunrise the dark woods seemed less scary and more magical. You both left arm in arm refreshed after creating lasting memories.")
            print()
            break
        elif path_3_3_3_choice != path_3_3_3_list[1] or path_3_3_3_choice != path_3_3_3_list[2]:
            print(random.choice(try_again))
        else:
            break


# Start Game Path
path()
