kalori = 0 

lari = input("Apakah kamu melakukan olahraga lari? jawab ya/tidak : ") == 'ya' 
if (lari): 
    menit = int(input("Berapa menit? ")) 
    kalori += menit*(60/5) 
pushUp = input("Apakah kamu melakukan olahraga push-up? jawab ya/tidak : ") == 'ya' 
if (pushUp):
    menit = int(input("Berapa menit? ")) 
    kalori += menit*(200/60) 
plank = input("Apakah kamu melakukan olahraga plank? jawab ya/tidak : ") == 'ya' 
if (plank): 
    menit = int(input("Berapa menit? ")) 
    kalori += menit*5 
    
kalori = round(kalori) 

if (kalori > 0): 
    print(f"\nKalori yang terbakar dari tubuhmu adalah {kalori} kalori") 
else: 
    print("\nTidak ada kalori yang terbakar, kamu tidak berolahraga : ")