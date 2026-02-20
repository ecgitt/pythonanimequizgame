# Declare repeat characters and backgrounds.
define q = Character("Quiz Master")
image bg room = "room.png"

# All audio.
define audio.correct = "audio/correct.mp3"
define audio.wrong = "audio/incorrect.mp3"
define audio.bgm = "audio/bgm.mp3"

# Start of the game.
label start:

    # Classroom.
    scene bg room
    show qhappy

    # Play the music.
    play music bgm loop

    # Integer for the player's grade at the end.
    $ score = 0

    # Opening dialogue.
    q "Welcome to the Ultimate Anime Quiz!"
    q "Identify each character correctly."

    # Goku Section.
    hide qhappy
    scene bg room
    show goku

    q "Who is this character?"
    menu:
        "Son Goku":
            play sound correct
            $ score += 1
            q "Correct! This is Son Goku."
        "Vegeta":
            play sound incorrect
            q "Wrong. This character is Son Goku."
        "Gohan":
            play sound incorrect
            q "Wrong. This character is Son Goku."
        "Bardock":
            play sound incorrect
            q "Wrong. This character is Son Goku."

    # Edward Elric Section.
    hide goku
    show edward

    q "Who is this character?"
    menu:
        "Alphonse Elric":
            play sound incorrect
            q "Wrong. This character is Edward Elric."
        "Edward Elric":
            play sound correct
            $ score += 1
            q "Correct! This is Edward Elric."
        "Roy Mustang":
            play sound incorrect
            q "Wrong. This character is Edward Elric."
        "Scar":
            play sound incorrect
            q "Wrong. This character is Edward Elric."

    # Light Yagami Section.
    hide edward
    show light

    q "Who is this character?"
    menu:
        "L":
            play sound incorrect
            q "Wrong. This character is Light Yagami."
        "Near":
            play sound incorrect
            q "Wrong. This character is Light Yagami."
        "Light Yagami":
            play sound correct
            $ score += 1
            q "Correct! This is Light Yagami."
        "Mello":
            play sound incorrect
            q "Wrong. This character is Light Yagami."

    # Naruto Section.
    hide light
    show naruto

    q "Who is this character?"
    menu:
        "Sasuke Uchiha":
            play sound incorrect
            q "Wrong. This character is Naruto Uzumaki."
        "Naruto Uzumaki":
            play sound correct
            $ score += 1
            q "Correct! This is Naruto Uzumaki."
        "Kakashi Hatake":
            play sound incorrect
            q "Wrong. This character is Naruto Uzumaki."
        "Minato Namikaze":
            play sound incorrect
            q "Wrong. This character is Naruto Uzumaki."

    # Ichigo Section.
    hide naruto
    show ichigo

    q "Who is this character?"
    menu:
        "Ichigo Kurosaki":
            play sound correct
            $ score += 1
            q "Correct! This is Ichigo Kurosaki."
        "Uryu Ishida":
            play sound incorrect
            q "Wrong. This character is Ichigo Kurosaki."
        "Renji Abarai":
            play sound incorrect
            q "Wrong. This character is Ichigo Kurosaki."
        "Byakuya Kuchiki":
            play sound incorrect
            q "Wrong. This character is Ichigo Kurosaki."

    # Luffy Section.
    hide ichigo
    show luffy

    q "Who is this character?"
    menu:
        "Monkey D. Luffy":
            play sound correct
            $ score += 1
            q "Correct! This is Monkey D. Luffy."
        "Ace":
            play sound incorrect
            q "Wrong. This character is Monkey D. Luffy."
        "Sabo":
            play sound incorrect
            q "Wrong. This character is Monkey D. Luffy."
        "Shanks":
            play sound incorrect
            q "Wrong. This character is Monkey D. Luffy."

    # Natsu Section.
    hide luffy
    show natsu

    q "Who is this character?"
    menu:
        "Gray Fullbuster":
            play sound incorrect
            q "Wrong. This character is Natsu Dragneel."
        "Erza Scarlet":
            play sound incorrect
            q "Wrong. This character is Natsu Dragneel."
        "Natsu Dragneel":
            play sound correct
            $ score += 1
            q "Correct! This is Natsu Dragneel."
        "Happy":
            play sound incorrect
            q "Wrong. This character is Natsu Dragneel."

    # Saber Section.
    hide natsu
    show saber

    q "Who is this character?"
    menu:
        "Saber":
            play sound correct
            $ score += 1
            q "Correct! This is Saber."
        "Rin Tohsaka":
            play sound incorrect
            q "Wrong. This character is Saber."
        "Illyasviel":
            play sound incorrect
            q "Wrong. This character is Saber."
        "Sakura Matou":
            play sound incorrect
            q "Wrong. This character is Saber."

    # Satoru Gojo Section.
    hide saber
    show gojo

    q "Who is this character?"
    menu:
        "Satoru Gojo":
            play sound correct
            $ score += 1
            q "Correct! This is Satoru Gojo."
        "Suguru Geto":
            play sound incorrect
            q "Wrong. This character is Satoru Gojo."
        "Yuji Itadori":
            play sound incorrect
            q "Wrong. This character is Satoru Gojo."
        "Megumi Fushiguro":
            play sound incorrect
            q "Wrong. This character is Satoru Gojo."

    # Sailor Moon section.
    hide gojo
    show sailormoon

    q "Who is this character?"
    menu:
        "Sailor Mars":
            play sound incorrect
            q "Wrong. This character is Sailor Moon."
        "Sailor Mercury":
            play sound incorrect
            q "Wrong. This character is Sailor Moon."
        "Sailor Moon":
            play sound correct
            $ score += 1
            q "Correct! This is Sailor Moon."
        "Sailor Jupiter":
            play sound incorrect
            q "Wrong. This character is Sailor Moon."

    stop music fadeout 1.0

    # Ending and grade plus game over.
    q "Quiz complete!"
    hide sailormoon
    show qhappy

    q "Your final score is [score] out of 10."
    q "Thanks for playing!"
    q "Farewell!"

    return
