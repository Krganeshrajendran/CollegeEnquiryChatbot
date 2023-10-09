import re
import long_responses as long
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_COURSE, ['what', 'are', 'the', 'course', 'in', 'cse', 'department'], required_words=['course', 'cse'])
    response(long.R_HOD, ['who', 'is', 'hod', 'of', 'cse','department'], required_words=['hod','cse'])
    response(long.R_DEPARTMENT, ['what','are','department','in','college'],required_words=['department','college'])
    response(long.R_PLACEMENTOFFICER, ['who','is','the','placement','officer'], required_words=['placement','officer'])
    response(long.R_STAFFNAME,['name','of','the','staff','name'],required_words=['staff','name'])
    response(long.R_STUDENTCOUNT, ['student','count','how','many','number'] , required_words=['student','count','numberhow '])
    response(long.R_LAB,['how','many','labs'],required_words=['lab'])
    response(long.R_SYSTEM, ['how','many','system','in','cse','department'],required_words=['system','cse'])
    response(long.R_PLACEMENTCOMPANY,['what','are','company','coming','from','cse','department'],required_words=['company'])
    response(long.R_COLLEGELOCATION,['location','of','the','college'],required_words=['location'])
    response(long.R_FEESSTRUCTURE,['what','is','the','fees','structure','of','this','college'],required_words=['fees','structure'])
    response(long.R_STUDENTPLACEMENT,['how','many','students','placed','in','previous','year','campus'],required_words=['placed','previous','year','campus'])




    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

@app.route('/bot', methods=['POST', 'GET'])
def bot():
    if request.method == 'POST':
        msg = request.form['you']
        res = get_response(msg)
        return render_template('index.html', res=res)    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
