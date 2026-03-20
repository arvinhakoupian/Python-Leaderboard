#1.creating a program that takes the file pad as an argument
#2. If file can't be open or invalid file USAGE: <program> <commands_file>
#3. execute non-empty lines
#4. ignoring commands starting with #
#5. Create ADD_PLAYER command if the player has empty history write None and if the player already exist print DUPLICATE
#6. Create ADD_SCORE command with 2 arguments first is name and the second one is score and if the player not found write NOT FOUND
#7. Create a CURRENT command Write players Recent Scores If none then NONE if Player not found then NOT FOUND
#8. Create a BEST command Write players best score if player not found then NOT FOUND if no score then NONE
#9. Create a HISTORY k command Write the first score if the player not found then NOT FOUND
#10. Create a TOP_K k command writing a snapshot leaderboard on the top with players by best score descending who have at least one score
#11. Create a PRINT_ALL command write all players sorting by best descending uing heap sort snapshot and players without scores will uppear at the end
#12. Create REMOVE_PLAYER name command removinf players and their entire history if not found then NOT FOUND
#13. Create LEN command writing current players registered
#14. Create Clear command removing all players and their histories
#15. Create QUIT command Exit