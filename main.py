from LanguageLoader import *
from RNN import *

en_path = 'data/en.zip'
fr_path = 'data/fr.zip'

max_length = 20
num_batches = 7500
vocab_size = 15000

def main():
    data = LanguageLoader(en_path, fr_path, vocab_size, max_length)
    rnn = RNN(data.input_size, data.output_size)

    losses = []
    for i, batch in enumerate(data.sentences(num_batches)):
        input, target = batch

        loss = rnn.train(input, target)
        losses.append(loss)

        if i % 100 is 0:
            print("Loss at step %d: %.2f" % (i, loss))
            rnn.save()

def translate():
    data = LanguageLoader(en_path, fr_path, vocab_size, max_length)
    rnn = RNN(data.input_size, data.output_size)

    vecs = data.sentence_to_vec("the president is here <EOS>")

    translation = rnn.eval(vecs)
    print(data.vec_to_sentence(translation))

#main()
translate()