import timeit
import HockeyLight.HockeyLight_GetScore
import HockeyLight.HockeyLight_HS

start_time = timeit.default_timer()
print(HockeyLight.HockeyLight_GetScore.getscore())
#print(HockeyLight.HockeyLight_HS.getscore())
elapsed = timeit.default_timer() - start_time
print(elapsed)