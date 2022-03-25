
class SocialMedia:
    def __init__(self, name: str, limitLen: int):
        self.__name = name
        self.__post_list = []
        self.__bodyLimitLen = limitLen
        
    def getName(self):
        return self.__name
        
    def _getPosts(self):
        return self.__post_list
        
    def _setPost(self, post: str):
        if self.__validateLen(post):
            self.__post_list.append(post)
    
    def __validateLen(self, post: str):
        return True if len(post) < self.__bodyLimitLen else False        
    
class Instagram(SocialMedia):
    def __init__(self):
        super().__init__("Instagram", 2200)
    
    def publishNewPost(self, post: str):
        super()._setPost(post)
            
    def getPosts(self):
        return super()._getPosts()
        
class Twitter(SocialMedia):
    def __init__(self):
        super().__init__("Twitter", 280)
    
    def getTwitts(self):
        return super()._getPosts()
        
    def publishNewTwitt(self, post: str):
        super()._setPost(post)
        
        
def show_socials_posts(socials: list):
    for social in socials:
        intro = social.getName()
        
        if intro == "Instagram":
            intro += " Posts: "
            print(intro,  social.getPosts())
        elif intro == "Twitter":
            intro += " Twitts: "
            print(intro,  social.getTwitts())
    
socials = []
socials.append(Instagram())
socials.append(Twitter())

show_socials_posts(socials)

socials[0].publishNewPost("Hi Instagram")
socials[1].publishNewTwitt("Hi Twitter")
socials[0].publishNewPost("Insta Is Worst Application For Life")

show_socials_posts(socials)



