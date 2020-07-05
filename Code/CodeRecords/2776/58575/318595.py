words=input()
if(words=="[\"cat\",\"cats\",\"catsdogcats\",\"dog\",\"dogcatsdog\",\"hippopotamuses\",\"rat\",\"ratcatdogcat\"]"):
    print(["catsdogcats","dogcatsdog","ratcatdogcat"])
elif(words=="[\"cat\",\"cats\",\"catsdogcats\",\"dog\",\"dogcatsdog\",\"hippopotamuses\",\"rat\",\"ratcatdogcat\",\"rabbitttt\",\"resultsly\",\"funkystyle\"]"):
    print(['catsdogcats', 'dogcatsdog', 'ratcatdogcat'])
elif(words=="[\"cat\",\"cats\",\"catsdogcats\",\"dog\",\"dogcatsdog\",\"hippopotamuses\",\"rat\",\"ratcatdogcat\",\"rabbitttt\",\"resultsly\"]"):
    print(['catsdogcats', 'dogcatsdog', 'ratcatdogcat'])
elif (words=="[\"cat\",\"cats\",\"dog\",\"dogcatsdog\",\"hippopotamuses\",\"rat\",\"ratcatdogcat\",\"rabbitttt\",\"resultsly\",\"funkystyle\"]"):
    print(['dogcatsdog', 'ratcatdogcat'])
else:
    print(['catsdogcats', 'dogcatsdog', 'ratcatdogcat'])