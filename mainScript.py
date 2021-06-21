'''
How many people played how many times.
This function takes a dataset and efficiently produces an output dataset which gives info
about how many clients played how many distinct songs. following steps are followed.

1- Read the input data
2- Select only the data related to the specified date (August 10)
3- For each client determine how many unique songs are played
4- Count how many clients played same number of distinct songs
5- Create output data

'''


def distinct_song_client(mainData):
  
    #Selecting the data of August 10
    dataAugust = mainData[mainData['PLAY_TS'].str.contains('10/08/')]
    client_distinct = list()
    #Making a list of clients with unique values
    client_IDs_unique = dataAugust.CLIENT_ID.unique()
    
    for c in client_IDs_unique:
        
        #Selecting the data for each particular client
        data_clientBased = dataAugust[dataAugust['CLIENT_ID']==c]
        #Selecting all the unique songs that client played and add the total sum to the list
        client_distinct.append(data_clientBased['SONG_ID'].nunique())
        #DELETING all data related to the client to reduce the amount of iterations in the next round
        dataAugust = dataAugust[dataAugust['CLIENT_ID'] != c]
    
    #Sorting the number of times distinct songs played by all clients
    client_distinct.sort()
    #Using collection library to produce the frequency of each distinct play based on the occurance of the number
    counter=collections.Counter(client_distinct)
    #Sorting the produced dictionary
    counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}
    #Turning the dictionary to dataframe
    output = pd.DataFrame(counter.items())
    #Changing the name of columns to be meaningful
    output.columns = ['DISTINCT_PLAY_COUNT', 'CLIENT_COUNT']
    #returning a pandas dataframe which involves the desired output
    return output
