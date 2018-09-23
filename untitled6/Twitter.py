from twitter import Twitter , OAuth , TwitterHTTPError
import random
t = Twitter(auth=OAuth('3893134475-MjuHWoGbzYmJv3ZuHaBvSENfyevu00NQuBc40VM','anJLBCOALCXl7aXeybmNA5oae9E03Cm23cKNMLaScuXwk','kl3E14NQx84qxO1dy247V0b2W','5VFVXVMq9bDJzFAKPfWOiYmJZin2F7YLhSfoyLBXf6Bc9ngX3g'))

t.search.tweets('sds',result_type='recent' , count=20)
t.search.tweets