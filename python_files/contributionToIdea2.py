
if __name__ == '__main__':
    playerCount = 500
    lValues = []
    lIndexes = [0]*playerCount
    scores = [0]*playerCount
    copyScore = scores
    copylIndexes = lIndexes
    for l in lValues:
        for player  in range(0,playerCount):
            if(scores[lIndexes[player]] > l): #burayı l'den küçük olan kadar devam ettirmemiz gerek
                copyScore[player] = copyScore[player] - scores[lIndexes[player]] + l
                copylIndexes[player] = copylIndexes[player]+1

        #check for final minimum place. If the new final place is better than the previous one
        lIndexes = copylIndexes
        scores = copyScore
