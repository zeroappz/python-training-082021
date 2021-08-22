'''
Management
9047048344 - praveen.p@zeroappz.com

Amusement Park: Money, Transport, members
    Family of 3 (2 adults and 1 kid) + pet animal
    1. Parking Area
        a) if(2whl or 4whl or bus) ----> (Rs. 30, 100, 500)
        b) availability ----> if yes: go ahead and pay: 
            else: wait for a while
        return parking_id, parking_amt_spent
    
    2. Ticketting:
        a) Adult - Rs. 750; Kid - Rs. 500; Pet animal - Rs. 100
        b) Total Hours to play (480 minutes) ----> No. of games to be played (12)
        return net amount spent, total_time, total_games
    
    3. Wet Games & Dry Games:
        a) common instructions ----> specific (roller coaster(30 min), bungee (45min))
        b) every game ----> (480 - 30) and (12-1)
        returns net games played in due time, time_wasted, games_not_played

    4. Snacks & Lunch -----> 3persons & dog
    

    Finally: 
        1) net games ---> what we played; what we missed
        2) net time  ---> how much spent; how much wasted
        3) Money spent overall

'''
