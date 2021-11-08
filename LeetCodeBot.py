import telebot
import requests
import json

API_KEY = '2108002255:AAFBH4mUle4-W66EVc0Pk9bOYS119Lz6Ym8'
bot = telebot.TeleBot(API_KEY)

def getData(username):
    query = """query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    username
    submitStats: submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
        submissions
      }
    }
  }
}"""
    variables = { "username": username }
    url = 'https://leetcode.com/graphql'
    r = requests.post(url, json={'query': query,'variables': variables})
    # print(r.status_code)
    ans = json.loads(r.text)
    msg = ""
    # print("ans",list(ans.keys())[0])
    # print("ans",ans['data'])
    if(list(ans.keys())[0] == "errors"):
        msg = "Please Enter Correct Username DumbFuck!!"
    else:
        msg = str(ans['data']['matchedUser']['username']) + " "+ "Solved "+ str(ans['data']['matchedUser']['submitStats']['acSubmissionNum'][1]['count']) + " Easy, "+ str(ans['data']['matchedUser']['submitStats']['acSubmissionNum'][2]['count'])+" Medium, "+ str(ans['data']['matchedUser']['submitStats']['acSubmissionNum'][3]['count'])+" Hard Problems!!"  
    return msg



@bot.message_handler()
def greet(message):
    # print(message.text[1:])
    bot.reply_to(message,getData(message.text[1:]))
    
    
bot.polling()
