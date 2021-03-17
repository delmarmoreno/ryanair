# Ryanair Test
In here you will find the code for a quick test in https://www.ryanair.com/ie/en. 
The test opens a chrome driver. 
We will go to te URL mentioned above, and will accept the cookie notice.
We will then select the type of flight to one way, per test requirements. 
We will select a from airport and to airport followed by some dates and number of passengers. 
From here, we will follow the flow of selecting and booking the flight up until payment.

I wasn't able to complete the payment process because I didn't want to have an actual account in production. 

# How to run: 

To run, open a terminal and type: behave features/ryanair.feature

Or you can simply type: behave 

# Dependencies
Make sure you have behave and selenium install. You can check this with:  pip list

If you don't see these services, you can type: pip install behave