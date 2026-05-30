from django.shortcuts import redirect, render
from django.contrib import messages as ms
from .models import Status, Game
import requests

def homepage(request):
    try:
        purchasedGames = Status.objects.get(username=request.user.username).purchasedGames
        purchaseId = Status.objects.get(username=request.user.username).purchaseId
    except Status.DoesNotExist:
        purchasedGames = None
        purchaseId = None
    games = Game.objects.all()

    if request.method == "POST":
        if not request.user.is_authenticated:
            ms.error(request, "Not logged in")
            return render(request,'homepage.html', {'purchasedGames': purchasedGames, 'purchaseId': purchaseId, 'games':games})

        Authorization = "ba9c15fa81fc2a4805a4d5032ec491c2f8bde939840e773690791ed15ea74204"

        sendrequest = requests.request("GET",  "https://daramet.com/api/LastDonates", headers={"Authorization": Authorization})
        jsondata = sendrequest.json()
        print("asda")
        for entry in jsondata:
            donate_amount = entry.get('donate_amount')

            message = entry.get('message')
            if purchaseId in message:
                print("aaa")
                try:
                    a = message.index(":")
                    game = message[:a]
                except:
                    continue
                game_status = Game.objects.get(id=game)
                if game in purchasedGames:
                    continue
                
                if donate_amount/10 == game_status.price:
                    getuser = Status.objects.get(username=request.user.username)
                    getuser.purchasedGames.append(int(game))
                    getuser.save()
                    purchasedGames = Status.objects.get(username=request.user.username).purchasedGames
                    ms.success(request, "Purchase successful! Thanks for buying our game!")
        
    return render(request,'homepage.html', {'purchasedGames': purchasedGames, 'purchaseId': purchaseId, 'games':games})



def unlock_game(request):
    if not request.user.is_authenticated:
        ms.error(request, "Not logged in")
    
    if request.method == "POST":
        game_name = request.POST.get("game_name")
        purchaseId = request.POST.get("purchaseId")
        if Game.objects.get(id=game_name).price == 0:
            user_status = Status.objects.get(username=request.user.username)
            user_status.purchasedGames.append(int(game_name))
            user_status.save()
            ms.success(request, f"{game_name} Unlocked for free! Thanks for playing our game!")
        return redirect('homepage')
