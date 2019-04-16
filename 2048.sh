#!/usr/bin/bash

while true
do
  function update_view () {
    clear
    ./src/view.py --board $board
  }

  if [[ $direction -eq 4 ]]; then
    >&2 echo "Invalid direction:" 
    >&2 echo "w: up, a: left, s: down, r: right" 
  elif [[ -z $board ]]; then
    board=$(./src/add_random.py --board "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
    update_view
  else
    board=$(./src/game.py "$direction" --board "$board" | ./src/add_random.py)
    update_view
  fi

  # Get input
  read -s -n1 key

  case "$key" in
    "w") direction=0;;
    "a") direction=2;;
    "s") direction=1;;
    "d") direction=3;;
    *) direction=4;;
  esac
done
