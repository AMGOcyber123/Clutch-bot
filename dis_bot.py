import discord
import time
import random
import time
client = discord.Client()

@client.command()
#@client.event
async def on_message(message):
####################################################### CHECKING IF BOT DOESNT REPLY ITSELF ############################
    message.content.lower()
    if message.author == client.user:
        return
###################################################### CASUAL REPLY TO MEMEBERS ########################################
    if message.content.startswith("hello"):
        await message.channel.send("hey, im a test bot.")
##################################################### SPECIAL REPLY TO CREATOR #########################################

    elif message.content.startswith("waddup") and str(message.author) == "hypegod101#3164":
        await message.channel.send("KONCHIWA")

######################################################## YOUTUBE CONNECTION ############################################

    elif message.content.startswith(";;play "):
        temp = ""
        intermediate = ""
        fin = ""
        c = 0
        k = len(message.content)
        for i in range(k):
            if message.content[i] == ' ':

                c += 1
                if c == 1:
                    intermediate = temp + " "
                    fin = message.content.replace(intermediate, "")
            else:
                temp = temp + message.content[i]

        await message.channel.send("https://www.youtube.com/results?search_query=" + fin.replace(" ", "+"))

################################################## TIMER ###############################################################

    elif message.content.startswith(";;set timer"):
        num = []
        await message.channel.send("DONE !")
        for word in message.content.split():
            if word.isdigit():
                num.append(int(word))
                for i in range(num[0]):
                    time.sleep(1)

        await message.channel.send("TIME UP !!!")

############################################## JOKES/TOUNGUE TWISTERS #################################################

    elif message.content.startswith(";;tell me a joke"):
        lis = [
            "What do you call a hippie's wife? A Mississippi!",
            "What did the duck say when she bought a lipstick? Put it on my bill!",
            "I hate Russian dolls. They're so full of themselves.",
            "What do you call a man with a rubber toe? Roberto!",
            "Where did the computer go dancing? The disc-o!",
            "What do bees do if they need a ride? Wait at the buzz stop!",
            "What do you give to a sick lemon? Lemon aid!",
            "What did the little mountain say to the bigger mountain? Hi Cliff!",
            "What do you call a monkey that loves Doritos? A chipmunk!",
            "Why did the can crusher quit his job? Because it was soda pressing!",
            "Why are there gates around cemeteries? Because people are dying to get in!",
            "What do you call a cow with two legs? Lean beef!",
            "Do you remember that joke I told you about my spine? It was about a weak back!",
            "I just went to an emotional wedding. Even the cake was in tiers.",
            "When's the best time to go to the dentist? Tooth-hurtie!",
            "What do you call a dangerous sun shower? A rain of terror!",
            "Why do seagulls fly over the sea? Because if they flew over the bay, they've bagels!",
            "What do you call a farm that makes bad jokes? Corny!",
            "Why do fish live in salt water? Because pepper makes them sneeze!",
            "What streets to ghosts haunt? Dead ends!"]
        joke = random.choice(lis)
        await message.channel.send(joke)
    elif message.content.startswith(";;tell me a pun"):
        lis2 = ["Light travels faster than sound. That's why some people appear bright until you hear them speak",
                "I was wondering why the ball was getting bigger. Then it hit me",
                "I have a few jokes about unemployed people, but none of them work",
                "\"I have a split personality\", said Tom, being frank.",
                "When life gives you melons, you're dyslexic",
                "Last night, I dreamed I was swimming in an ocean of orange soda. But it was just a Fanta sea",
                "Will glass coffins be a success? Remains to be seen",
                "It's hard to explain puns to kleptomaniacs because they always take things literally",
                "I lost my job at the bank on my very first day. A woman asked me to check her balance, so I pushed her over",
                "What’s the difference between a hippo and a zippo? One is really heavy and the other is a little lighter",
                "Two windmills are standing in a wind farm. One asks, \"What’s your favorite kind of music?\" The other says, \"I’m a big metal fan.\"",
                "Did you hear about the guy whose whole left side was cut off? He’s all right now",
                "I tried to sue the airline for losing my luggage. I lost my case",
                "A police officer just knocked on my door and told me my dogs are chasing people on bikes. That’s ridiculous. My dogs don’t even own bikes",
                "Which country’s capital has the fastest-growing population? Ireland. Every day it’s Dublin",
                "How do you throw a space party? You planet",
                "My ex-wife still misses me. But her aim is starting to improve",
                "The other day I tried to make a chemistry joke, but got no reaction",
                "What do you call an alligator in a vest? An investigator",
                "Need an ark? I Noah guy",
                "German sausage jokes are just the wurst",
                "I used to be indecisive; now I'm not so sure",
                "I like European food so I decided to Russia over there because I was Hungary. After Czech'ing the menu I ordered Turkey. When I was Finnished I told the waiter \'Spain good but there is Norway I could eat another bite\'",
                "Why are frogs so happy? They eat whatever bugs them",
                "The machine at the coin factory just suddenly stopped working, with no explanation. It doesn’t make any cents"]
        pun = random.choice(lis2)
        await message.channel.send(pun)
################################################# ARITHMETIC OPERATION ################################################
    elif message.content.startswith(";;add "):       ######## ADDITION ########
        num=[]
        for number in message.content.split():
            if number.isdigit():
                num.append(int(number))
        test = len(num)
        sum=0
        for i in range(test):
            sum+=num[i]
        await message.channel.send(sum)


client.run('NzUwNDE5Nzc4ODQ1NTQwNDAz.X06Q4Q.O2Ib4jzzTAD6bjjd9mteJpmq-3c')







##################################################
###          COMMANDS FOR CLUTCH BOT           ###
###   1. ;;play = direct link to the video     ###
###   2. ;;set timer                           ###
###   3. ;;tell me a joke                      ###
###   4.;;tell me a pun                        ###
###   5. hello = gives a casual response       ###
###                                            ###
##################################################