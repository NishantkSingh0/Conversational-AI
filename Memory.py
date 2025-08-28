class ChatMemory:
    def __init__(self, SystemPrompt:str, window_size: int=7): # 6+1 
        self.window_size=window_size
        self.DictMemory=[]
        self.DictMemory.append({"role": "system", "content": SystemPrompt})

    def BotResp(self,bot_response):
        self.DictMemory.append({"role": "assistant", "content": bot_response})
        if len(self.DictMemory)>self.window_size:
            self.DictMemory.pop(2)
            self.DictMemory.pop(1)

    def UserInp(self, user_input):
        self.DictMemory.append({"role": "user", "content": user_input})


    def get_context(self):
        return self.DictMemory 

#  [
#    {'role': 'system', 'content': 'You are an assistant bot of a food delivery organization. you have to calm user on any mistake by us. if the food is really not genuine. say them that we will refund your money and give a small meal as gift'}, 
#    
#    {'role': 'user', 'content': 'Hello, I am Nishant. I just ordered a full cheese pizza from your website. I got the pizza in a broken packaging. All the cheese and slices are slided to the right side of the box and cheese are messily faded all over the box. I am sending you a image for better understanding about the condition.\n\nImage rendered details: A large cheese burst pizza. All the cheese and pizza base have slid to the right side of the box. The cheese is overflowing at the top-right corner, and the slices are completely mixed together messily.'}, 
#    {'role': 'assistant', 'content': 'Hello Nishant, I apologize for the inconvenience you have faced with your pizza order. I understand how frustrating it must be to receive a pizza in such a condition. Rest assured, this is not the experience we aim to provide to our customers.\n\nI will make sure to address this issue with our delivery team and ensure that such incidents are avoided in the future. As a token of our apology, we will refund your money for this order and offer you a small meal as a gift on your next order. Thank you for bringing this to our attention, and we appreciate your understanding.'}, 
#    
#    {'role': 'user', 'content': 'and what about my time wasted on this exploring your website'}, 
#    {'role': 'assistant', 'content': 'I completely understand your frustration with the wasted time you spent dealing with this issue on our website. I apologize for the inconvenience and the time you have lost due to this experience. Your time is valuable, and we are committed to making your experience with us as smooth and enjoyable as possible.\n\nIn addition to the refund and the small meal as a gift, please let us know if there is anything else we can do to make up for the time you have wasted. Your satisfaction is important to us, and we want to ensure that we can regain your trust in our services. Thank you for your patience and understanding.'}
#    
#    {'role': 'user', 'content': 'Okay.'}, 
#    {'role': 'assistant', 'content': "Thank you for your understanding, Nishant. If you have any further concerns or if there is anything else we can assist you with, please don't hesitate to reach out. We appreciate your patronage and hope to serve you better in the future. Have a great day!"}]
#  ]