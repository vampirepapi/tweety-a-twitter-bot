
<h1 align="center">MojitoPapi 🤖 </h1> 
<div align= "center">
  <h4>A Twitter Bot that automatically retweets, favourites the tweets that are related to Technology, Programming & Python
</div>


## Follow us on Twitter - Click [mojito_papi](https://twitter.com/mojito_papi)

### :star: Star us on GitHub — it motivates me a lot!


<p align="center"><img src="https://github.com/vampirepapi/mojitopapi---a-bionic-alterego/blob/master/images/scrennshot.JPG"></p>



## 🚀&nbsp; Installation

#### Clone the repo
```
$ git clone https://github.com/vampirepapi/mojitopapi---a-bionic-alterego.git
```

#### Install tweepy Python module
```
$ pip install tweepy
```
## :bulb: Working

### Sign up for a Twitter Developer Account
* Create a separate Twitter account for your bot.
* Sign up for Twitter Developer Account from this site - [Apply for a Twitter Developer Account](https://developer.twitter.com/en/apply-for-access)
* Enter the necessary fields and await for email confirmation.
* Click on [Create an app](https://developer.twitter.com/en/apps)
* Enter the details and keep safe the access tokens generated.


#### Enter your generated access tokens and consumer keys in the file <code>credentials.py</code>

```
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```
#### Edit the retweet and other details in the file <code>app.py</code>(located in the end of <code>app.py</code>)

```
# This is hastag which Twitter bot will search and retweet. You can edit this with any hastag .For example : '#javascript'
hashtag = ['#python','#programming','#dsa','#100daysofcode','#PythonProgramming','#algorithms','#MachineLearning','#AI','#DataScience','#cpp','#c++','#codechef','#Flask','#django','#stackoverflow','#cybersecurity','#githubcopilot']


# Twitter bot sleep time settings in seconds. For example SLEEP_TIME = 600 means 10 minutes.
# you can decrease it or increase it as you like.Please,use large delay if you are running bot all the time  so that your account does not get banned.

SLEEP_TIME = 600
```

## :key: Deployment

* Sign up for a free account in [Heroku](heroku.com)
* Click on New -> Create new app
* Enter the app-name in lower case and select your nearest region.
* Connect with your github repo and build.
* Once the build is successful enable the Free Dynos option from Overview tab.





##  :wolf: Contributor
Made :heart: by   [vampirepapi](https://github.com/vampirepapi)
