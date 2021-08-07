import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("enter the city to show the data\n chicago\n new york city\n washington\n").lower()
    #validation of city_name
    while city not in CITY_DATA.keys():
        print("this city name is not valid")
        city=input("enter the city to show the data\n chicago\n new york city\n washington\n").lower()
   
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june','all']
    month=input("do you want a month in the first half of the year or all:\n january\n, february\n,march\n,april\n,may\n,june\n,all\n").lower()
    #validation of month_name
    while month not in months:
        print("this month name is not valid")
        month=input("do you want a month in the first half of the year or all:\n january\n, february\n,march\n,april\n,may\n,june\n,all\n").lower()
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=["sat","sun","mon","tue","wed","thu","fri","all"]
    day=input("do you want a specific day or all days of the week \n sat\n,sun\n,mon\n,tue\n,wed\n,thu\n,fri\n,all\n").lower()
    #validation of day name
    while day not in days:
        print("this day name is not valid")
        day=input("do you want a specific day or all days of the week \n sat\n,sun\n,mon\n,tue\n,wed\n,thu\n,fri\n,all\n").lower()
    
    print('-'*40)
    return city, month,day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Read Data as pandas Dataframe
    df=pd.read_csv(CITY_DATA[city])
    
    #convert column of Start Time to show the hour
    df['Start Time']=pd.to_datetime(df["Start Time"])
    df['hour'] = df['Start Time'].dt.hour

    #Extract month & month name from the column of Start Time
    df["month"] = df["Start Time"].dt.month
    df['month name'] = pd.DatetimeIndex(df['Start Time']).month_name()

    # filter by month name:
    if month != 'all':
       df = df[df["month name"].str.startswith(month.title())]
    
    #Extract day name from the column of Start Time
    df["day of week"] = df["Start Time"].dt.day_name()
    # filter by day of week:
    if day != 'all':
       df = df[df["day of week"].str.startswith(day.title())]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    Most_common_month = df['month'].mode()[0]
    print("most common month is ",Most_common_month)

    # TO DO: display the most common day of weekdf[]=df[].mode().[0]
    
    Most_common_day = df['day of week'].mode()[0]
    print("most common day is ",Most_common_day)
    # TO DO: display the most common start hour
    most_common_start_hour=df['hour'].mode()[0]
    print("most common hour is ",most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_start_station = df["Start Station"].mode()[0]
    print("commonly used start station is: ",commonly_used_start_station)
    # TO DO: display most commonly used end station
    commonly_used_end_station = df["End Station"].mode()[0]
    print("commonly used End Station is: ",commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["End Station"]+df["Start Station"]
    commonly_combination = df["combination"].mode()[0]
    print("most frequent combination is: ",commonly_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #convert column of End Time to show the duration
    df['End Time']=pd.to_datetime(df["End Time"])
    
    df["trip duration"]=df["End Time"]-df["Start Time"]
    # TO DO: display total travel time in minutes

    df["trip duration"] = df["trip duration"]/np.timedelta64(1,"m")
    #summing travel Duration
    total_travel_time = round(df["trip duration"].sum(),1)
    print("Total Travel Time: ",total_travel_time,"minute")
    # TO DO: display mean travel time
    mean_travel_duration = round(df["trip duration"].mean(),1)
    print("mean travel duration",mean_travel_duration,"minute")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    # TO DO: Display counts of user types
    
    start_time = time.time()
    counts_of_user_types=df["User Type"].value_counts()
    print("the counts of user Types\n",counts_of_user_types)
      
     # TO DO: Display counts of gender,earlist birth year,most recent birth year and most common birth year if                                    the columns of Gender andnbirth date are available  
    
    try:
        counts_gender = df["Gender"].value_counts()
        print("counts of Gender is:\n",counts_gender)
        earlist_birth_year = int(df["Birth Year"].min())
        print("earlist birth year is",earlist_birth_year)
        most_recent_birth_year = int(df["Birth Year"].max())
        print("most recent birth year is",most_recent_birth_year)
        common_birth_year = int(df["Birth Year"].mode()[0])
        print("most common birth year is",common_birth_year)
    except:
        print("gender and birth date info isn\'t available for this city")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_display(city):
    """
    Display raw data if user want
    
    """
#displying five rows of raw data if the user want that
    raw_data=input("do you want to show 5 rows from the raw data?").lower()
    while raw_data=="yes":
        for chunk in pd.read_csv(CITY_DATA[city], chunksize=5):   
            pd.set_option('display.max_columns',200)
            print(chunk)
            raw_data=input("do you want to show another 5 rows from raw data?").lower()
            if raw_data == "no":
                break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        data_display(city)
        restart = input('\nWould you like to restart?\n')
        if restart.lower() != ('yes' and 'no'):
            print("invalid input")
        elif restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
