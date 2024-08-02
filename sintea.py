df['FilteredMentions'] = df.apply(lambda x: [ele for ele in x['PostMention'] if ele != x['PosterID']], axis=1)
