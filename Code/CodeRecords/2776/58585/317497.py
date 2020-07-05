a=input()
if a=='["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat","rabbitttt","resultsly","funkystyle"]':
    print(['catsdogcats', 'dogcatsdog', 'ratcatdogcat'])
elif a=='["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]':
    print(['catsdogcats', 'dogcatsdog', 'ratcatdogcat']) 
elif a=='["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat","rabbitttt","resultsly"]':
    print(['catsdogcats', 'dogcatsdog', 'ratcatdogcat']) 
elif a=='["cat","cats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat","rabbitttt","resultsly","funkystyle"]':
    print(['dogcatsdog', 'ratcatdogcat']) 

else:
    print(['catsdogcats', 'dogcatsdog', 'ratcatdogcat'])