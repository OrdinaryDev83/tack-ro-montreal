#!/bin/bash

P=0
F=0

echo -e "\e[48;5;172mTest Suite : 1 étude du cas théorique\e[49m"
echo -e "------------------------------------------------------"

for filename in test_*.py; do
    [ -e "$filename" ] || continue
    python3 "$filename"
    R=$?
    if [[ $R -eq 0 ]]
    then
        echo -e "\e[100m${filename}\e[49m ✔️"
        P=$((P+1))
    else
        echo -e "\e[100m${filename}\e[49m ❌"
        F=$((F+1))
    fi
    echo -e "------------------------------------------------------"
done

echo -e "\e[48;5;172mRésultat :\e[49m"
echo "$P ✔️"
echo "$F ❌"