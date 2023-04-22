import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]

train_acc = [0.6919811349239419,0.6947891568083963,0.7116735206555674,0.7173137194514393,0.7307016431457092,0.7246508088914654,0.735200516917577,0.7399530184725569,0.7380326938289945,0.7410326938289945]
dev_acc = [0.725,0.722,0.728,0.738,0.742,0.739,0.749,0.747,0.747,0.754]
test_acc = [0.734,0.725,0.735,0.754,0.748,0.743,0.744,0.754,0.752,0.761]

train_loss = [0.006429068205829197,0.005846346895299691,0.00547871908886931,0.005342081495218117,0.005283738874939704,0.005291946216484955,0.004972102571605565,0.0050286022031109726,0.005014021710710027,0.00499207229167223]
dev_loss = [0.005866888270247728,0.005265613668598235,0.005123373295646161,0.004892434226348996,0.005065533157903701,0.005082790099550039,0.004788768186699599,0.0048486228042747825,0.004873973375651985,0.004771685576997697]
test_loss = [0.005736283143050969,0.005332030646968633,0.00512726535089314,0.0049897326971404254,0.00501352472929284,0.004946265049511567,0.004805804608622566,0.004841651243623346,0.004886095004621893,0.004798390262294561]

time = [248.6087188720703,249.3597071170807,249.84105348587036,249.3739092350006,248.98597240447998,248.13881587982178,247.64714550971985,248.13863015174866,247.54362082481384,248.98597240447998]


# plt.plot(x, train_loss, label = "Training loss")
# plt.plot(x, dev_loss, label = "Dev loss")
# plt.plot(x, test_loss, label = "Testing loss")
# plt.legend()

# plt.title('Loss v/s Epoch for Bi-LSTM with 3 hidden layers')
# plt.xlabel('Epoch Number')
# plt.ylabel('Loss')
# plt.savefig('loss_bilstm_3.png')

Time = []
acc = 0
for i in range(len(time)):
    acc+=time[i]
    Time.append(acc)

avg = acc/len(time)

plt.plot(x, Time, label = "Average Time Taken for 1 Epoch = {}".format(avg))
plt.legend()
plt.title('Time elapsed v/s Epoch for Bi-LSTM with 3 hidden layers')
plt.xlabel('Epoch Number')
plt.ylabel('Time (in seconds)')
plt.savefig('time_bilstm_3.png')
