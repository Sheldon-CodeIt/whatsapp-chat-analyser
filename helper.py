from urlextract import URLExtract

extractor = URLExtract()


def fetchStats(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
    words = []
    for message in df['message']: 
        words.extend(message.split())
    num_words = len(words)

    # fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]
        
    # fetch number of links shared
    links = []
    for message in df['message' ]:
        links.extend(extractor.find_urls(message))
    num_links = len(links)


    return num_messages, num_words, num_media_messages, num_links


# fetch most busy users
def most_busy_users(df):
    x = df['user'].value_counts().head()
    df_chat_percent = round((df['user'].value_counts()/df.shape[0])*100, 2).reset_index().rename(columns={'user': 'name', 'count': 'percent'})
    
    return x, df_chat_percent