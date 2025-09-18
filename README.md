# User manual for game-keys.

The code was writed in spanish maybe you will learn some new words, surprise you didnt know that. And basically we have 1 main script and 3 python modules i create.

## Games_keys.py

The main file is Games_keys.py i call it "the frontend"

Is where the code works, inside Games_keys.py here i use the list module that i create(not aditional pip install step if using all the directory), you have an infinite loop after running the functions unless you wite something else instead of enter.

## list.py

I call list.py "the brain" is where the main funtions agregar_juego(add a new game to the data base) and canjear_clave(where you can use a key to "obtain" your game) works and i use the modules os, csv,  ast and clasificacion(i create this last module because is important). You can create a game key with some questions about your game or simply exchange your game with a game key. Its important to follow all the steps to have the code working well. Here in agregar_juego() function is where the keys and all stuff related with the game is assigned to the datos.csv (You cant choose the file name yet maybe in the future). And most important agregar_juego() function is where you add the game to the csv.

## clasificacion.py

I call clasificacion.py "the skeleton" because is the main structure/framework of the program. Its not a surprise that is the has the most lines of code, comparing to the other 3 scripts. Basically here for adding games we have the functions to ask the game genre, year, platform, name, game kind, and some things related with the game of the year and deppending on the principal options or the user input it creates . We have another function where the game key is generated and use the first functions to create that key. And the last function canjeo() is where you confirm the key, if its correct or not  what you write, basically its not important at all but because a module call metodology i need that "irrelevar" function over there, its important to not call an extra module in list.py, but basically the canjeo() function, the instructions inside are a little bit irrelevant. Inside all that functions including the "irrelevant" canjeo() i call a function form the last module valor_valido.py but i´ll explain that later. At last but not least i use the valor_valido as vv module(i create that module surprise you didnt know that).

## valor_valido.py

The last module valor_valido.py, i call it "the bone calcium" its not important... at all because i mean the calcium is important for the bones with with not that much they´re okay. Basically valor_valido.py is 1 function that only recives the user input form every game aspect like year, name, genre, etc. This module it´s not that relevant... at all because the only work its to control the user inputs, that they only use the alowed characters line letters, numbers, space and ñ. Of course ñ, i also speak spanish. Btw i use a if because depending form the game characteristic it only needs for example name letters and also numbers because some games use numbers, but for example years could only recive numbers, and thats all. I lied to you, well not at all. I said that this module its not that important, it takes care(a little) of the game characteristic inputs and the key creation, only to recieve the allowed characters. But its important only this case because i put the input from every game characteristic here. It couldnt be that important if you change the game characteristic input in clasificacion.py for example but it´ll not have this control to prevent the invalid characters. Here i used re module(I create re too in the past. Nah just kidding i didint re but you owe me 5 dollars if i catch you :p).

## Important things.

Basically  for Games_keys.py to work correclty you need list.py and fot list.py you need clasificacion.py and last but not least clasificacion.py needs valor_valido.py to worl properly. Its like a chain, thats because all the brain, bones, etc. similitudes and well another modules that i didnt create but i use it in some of the scripts.

## Simulation.

It is important to know that the code itself creates, if it does not exist, a file called datos.csv with initial values in the first row in list format, which are: [gender, year, platform, name, type, result, game_key].

The code basically with each record made in the main (Games_keys.py) in the function agregar_juego() will save in the next row to the last a new row of data now with the data itself in the csv file to classify the added game and will print on the screen a key that we can use later. Later, if we use the redeem_key() function in the main, it will ask us for a game key, whether we received it in add_game() or from anywhere else. But when we redeem the key and it is correct, it will display a text with the metadata of our game based on the key we gave it.
