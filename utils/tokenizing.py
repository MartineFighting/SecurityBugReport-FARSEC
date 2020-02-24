import nltk
import re


def is_unwanted(word):
    '''
    :param word: 需要判断的word
    :return: True represent the word is unwanted
    '''
    # 是否标点符号
    is_punctuation = re.search("(?i)[\w]+", word)
    if is_punctuation == None:
        return True
    # 是否字母数字
    is_alphanumeric = re.search("\d+", word)
    if is_alphanumeric:
        return True
    # 是否包含下划线
    is_underscore = re.search("_", word)
    if is_underscore:
        return True
    # 是否包含url
    is_url = re.match("//", word)
    if is_url:
        return True
    is_unletters = re.search("[^a-zA-Z]", word)
    if is_unletters:
        return True
    return False


def unwanted_words(word):
    '''
    Removes unwanted keywords, such as urls, alphnumeric, underscores, punctuation, stopwords and single characters.
    :param word:
    :return: if word is meaningful, then return True else return False
    '''
    # Remove stop words
    stopwords = set(nltk.corpus.stopwords.words('english'))
    if word in stopwords:
        return False
    # Remove unwanted word
    if is_unwanted(word):
        return False
    # Remove the length of word less than 3
    if len(word) < 3:
        return False
    return True


# Processing the text of BugReport
def preprocess_br(raw_description):
    # print(raw_description)
    # 1. Tokenize
    current_desc_tokens = nltk.word_tokenize(raw_description)
    # 2. normalize (Change to lower case)
    lower_desc_tokens = [w.lower() for w in current_desc_tokens]
    # 3. unwanted words
    meaningful_words = [w for w in lower_desc_tokens if unwanted_words(w)]
    return meaningful_words


if __name__ == '__main__':
    raw_text = "Setup LDAP does not validate true/false response   Garbage responses to true/false questions just pass thru. Notice below  just put in garbage for Use SSL and that's what it would have written.Need validation to confirm they enter either 1) return to accept default or 2) the word true or 3) the word false. Else  inform the user'Property must be 'true' or 'false'.' and ask again.Secondary URL :Use SS &#91;true/false&#93; (false): asdUser name attribute* (uid):Base DN* :Property cannot be blank.Base DN* : asdBind anonymously* true/false (false):Manager DN* :asdEnter Manager Password*:Re-enter password:Passwords do not matchEnter Manager Password*:Re-enter password:====================Review Settings====================authentication.ldap.primaryUrl: my.url:849authentication.ldap.useSSL: asdauthentication.ldap.usernameAttribute: uid"
    result = preprocess_br(raw_text)
    print(result)
