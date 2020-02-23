import numpy as np
import json
from matplotlib import pyplot as plt
####################################### ~> Load and Visualise Data

with open('testing_data.json','r') as f:
    #data_test = f.read()
    validation_dict = json.load(f)

with open('training_data.json', 'r') as g:
    #data_train = g.read()
    train_dict = json.load(g)

tatls_dict = {"title": [], "id": [], "body": [],
              "score": [], "subreddit": [], "best_comment": [],
              "second_best_comment": []}

for n, (title, ID,body,score,subreddit,best_comment, second_best_comment ) in enumerate(train_dict):
    tatls_dict["title"].append(train_dict[n]["title"])
    tatls_dict["id"].append(train_dict[n]["id"])
    tatls_dict["body"].append(train_dict[n]["body"])
    tatls_dict["score"].append(train_dict[n]["score"])
    tatls_dict["subreddit"].append(train_dict[n]["subreddit"])
    tatls_dict["best_comment"].append(train_dict[n]["best_comment"])
    tatls_dict["second_best_comment"].append(train_dict[n]["second_best_comment"])


#print("Tatl says: "+ str(len(tatls_dict["title"])))
print(tatls_dict["id"])

print("Training data: "  + str(len(train_dict)))
print("Validation data: " + str(len(validation_dict)))
MAX_LENGTH = len(train_dict)
############################################################ ~> Convert to Lower Case
print(tatls_dict["body"])
body_text = [body.lower() for body in tatls_dict["body"]]
#print(body_text)
########################################################## ~> Remove Punctuation
from string import punctuation
#print(body_text)
print("\n### Punctuation ###\n")
print(punctuation)
all_text = ''.join([c for c in body_text if c not in punctuation])
#print(all_text)
########################################################### ~> create review list
body_split = all_text.split('\n')
print("Number of body_text: ", len(body_split))
########################################################### ~> Tokenizing v->to->I map dict
from collections import Counter

all_text_2 = ''.join(body_split)
words = all_text_2.split()
word_count = Counter(words)
val = len(words)
sorted_words = word_count.most_common(val)
#print(word_count)

vocab_to_int = {w:i+1 for i, (w,c) in enumerate(sorted_words)}
print(vocab_to_int)
########################################################### ~> Tokenizing: Encoding Words
body_int = []
msg_list = body_split
print(msg_list)
for b in body_split:
    r = [vocab_to_int.get(w) for w in b]
    body_int.append(r)
print (body_int[0:3])

########################################################### ~> Tokenizing: Encoding labels
encoded_labels = [1 if label=='positive' else 0 for label in validation_dict]
encoded_labels = np.array(encoded_labels)
print(encoded_labels)
########################################################## ~> Analyse reviews lengths
import pandas as pd
body_len = [len(x) for x in body_int]
pd.Series(body_len).hist()
#plt.show()

pd.Series(body_len).describe()
############################################################### ~> Reduce outliers
body_int = [ body_int[i] for i, l in enumerate(body_len) if l>0 ]
#encoded_labels = [ encoded_labels[i] for j, l in enumerate(body_len) if l> 0 ]




############################################################### ~> Padding features
def pad_features(body_int, seq_length):
    ''' Return features of review_ints, where each review is padded with 0's or truncated to the input seq_length.
    '''
    features = np.zeros((len(body_int), seq_length), dtype = int)

    for i, tatls_dict["body"] in enumerate(body_int):
        body_len = len(tatls_dict["body"])

        if body_len <= seq_length:
            zeroes = list(np.zeros(seq_length-body_len))
            new = zeroes+tatls_dict["body"]
        elif body_len > seq_length:
            new = tatls_dict["body"][0:seq_length]

        features[i,:] = np.array(new).astype(np.float32)

    print(features.shape)
    return features

features = pad_features(body_int,2)

##################################################################
split_frac = 0.8
len_feat = len(features)
train_x = features[0:int(split_frac*len_feat)]
train_y = encoded_labels[0:int(split_frac*len_feat)]
remaining_x = features[int(split_frac*len_feat):]
remaining_y = encoded_labels[int(split_frac*len_feat):]
valid_x = remaining_x[0:int(len(remaining_x)*0.5)]
valid_y = remaining_y[0:int(len(remaining_y)*0.5)]
test_x = remaining_x[int(len(remaining_x)*0.5):]
test_y = remaining_y[int(len(remaining_y)*0.5):]
###################################################################
import torch
from torch.utils.data import DataLoader, TensorDataset
train_data = TensorDataset(torch.from_numpy(train_x), torch.from_numpy(train_y))
valid_data = TensorDataset(torch.from_numpy(valid_x), torch.from_numpy(valid_y))
test_data = TensorDataset(torch.from_numpy(test_x), torch.from_numpy(test_y))

batch_size = 50

train_loader = DataLoader(train_data, shuffle=True, batch_size=batch_size)
valid_loader = DataLoader(valid_data, shuffle=True, batch_size=batch_size)
test_loader = DataLoader(test_data, shuffle=True, batch_size=batch_size)

# obtain one batch of training data
dataiter = iter(train_loader)
sample_x, sample_y = dataiter.next()
print('Sample input size: ', sample_x.size()) # batch_size, seq_length
print('Sample input: \n', sample_x)
print('Sample label size: ', sample_y.size()) # batch_size
print('Sample label: \n', sample_y)


class SentimentLSTM(nn.Module):
    """
    The RNN model that will be used to perform Sentiment analysis.
    """

    def __init__(self, vocab_size, output_size, embedding_dim, hidden_dim, n_layers, drop_prob=0.5):
        """
        Initialize the model by setting up the layers.
        """
        super().__init__()

        self.output_size = output_size
        self.n_layers = n_layers
        self.hidden_dim = hidden_dim

        # embedding and LSTM layers
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, n_layers,
                            dropout=drop_prob, batch_first=True)

        # dropout layer
        self.dropout = nn.Dropout(0.3)

        # linear and sigmoid layers
        self.fc = nn.Linear(hidden_dim, output_size)
        self.sig = nn.Sigmoid()


    def forward(self, x, hidden):
        """
        Perform a forward pass of our model on some input and hidden state.
        """
        batch_size = x.size(0)

        # embeddings and lstm_out
        embeds = self.embedding(x)
        lstm_out, hidden = self.lstm(embeds, hidden)

        # stack up lstm outputs
        lstm_out = lstm_out.contiguous().view(-1, self.hidden_dim)

        # dropout and fully-connected layer
        out = self.dropout(lstm_out)
        out = self.fc(out)
        # sigmoid function
        sig_out = self.sig(out)

        # reshape to be batch_size first
        sig_out = sig_out.view(batch_size, -1)
        sig_out = sig_out[:, -1] # get last batch of labels

        # return last sigmoid output and hidden state
        return sig_out, hidden


    def init_hidden(self, batch_size):
        ''' Initializes hidden state '''
        # Create two new tensors with sizes n_layers x batch_size x hidden_dim,
        # initialized to zero, for hidden state and cell state of LSTM
        weight = next(self.parameters()).data

        if (train_on_gpu):
            hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().cuda(),
                  weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().cuda())
        else:
            hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_(),
                      weight.new(self.n_layers, batch_size, self.hidden_dim).zero_())

        return hidden


# Instantiate the model w/ hyperparams
vocab_size = len(vocab_to_int)+1 # +1 for the 0 padding
output_size = 1
embedding_dim = 400
hidden_dim = 256
n_layers = 2

net = SentimentLSTM(vocab_size, output_size, embedding_dim, hidden_dim, n_layers)

print(net)

SentimentLSTM(
  (embedding): Embedding(74073, 400)
  (lstm): LSTM(400, 256, num_layers=2, batch_first=True, dropout=0.5)
  (dropout): Dropout(p=0.3)
  (fc): Linear(in_features=256, out_features=1, bias=True)
  (sig): Sigmoid()
)


# loss and optimization functions
lr=0.001

criterion = nn.BCELoss()
optimizer = torch.optim.Adam(net.parameters(), lr=lr)


# training params

epochs = 4 # 3-4 is approx where I noticed the validation loss stop decreasing

counter = 0
print_every = 100
clip=5 # gradient clipping

# move model to GPU, if available
if(train_on_gpu):
    net.cuda()

net.train()
# train for some number of epochs
for e in range(epochs):
    # initialize hidden state
    h = net.init_hidden(batch_size)

    # batch loop
    for inputs, labels in train_loader:
        counter += 1

        if(train_on_gpu):
            inputs, labels = inputs.cuda(), labels.cuda()

        # Creating new variables for the hidden state, otherwise
        # we'd backprop through the entire training history
        h = tuple([each.data for each in h])

        # zero accumulated gradients
        net.zero_grad()

        # get the output from the model
        inputs = inputs.type(torch.LongTensor)
        output, h = net(inputs, h)

        # calculate the loss and perform backprop
        loss = criterion(output.squeeze(), labels.float())
        loss.backward()
        # `clip_grad_norm` helps prevent the exploding gradient problem in RNNs / LSTMs.
        nn.utils.clip_grad_norm_(net.parameters(), clip)
        optimizer.step()

        # loss stats
        if counter % print_every == 0:
            # Get validation loss
            val_h = net.init_hidden(batch_size)
            val_losses = []
            net.eval()
            for inputs, labels in valid_loader:

                # Creating new variables for the hidden state, otherwise
                # we'd backprop through the entire training history
                val_h = tuple([each.data for each in val_h])

                if(train_on_gpu):
                    inputs, labels = inputs.cuda(), labels.cuda()

                inputs = inputs.type(torch.LongTensor)
                output, val_h = net(inputs, val_h)
                val_loss = criterion(output.squeeze(), labels.float())

                val_losses.append(val_loss.item())

            net.train()
            print("Epoch: {}/{}...".format(e+1, epochs),
                  "Step: {}...".format(counter),
                  "Loss: {:.6f}...".format(loss.item()),
                  "Val Loss: {:.6f}".format(np.mean(val_losses)))


#build Tensors




#print(body_split)

# for data in data_dict:
#     print(data['score'])
#print(data_dict[]['title'])
# dictionary[page][feature]

#KEYS:
# Title ~> description summary
# id ~> reference to file
# body ~> has the actual content for SA
# score ~> representation of popularity
# subreddit ~> segment/feature of belonging
# best_comment ~> potential best response
# second_best_comment ~> potential runner-up repoonse
