# import tensorflow as tf
import tensorflow.compat.v1 as tf
import os

FLAGS = tf.app.flags.FLAGS


# FLAGS = tf.app.flags.FLAGS
# tf.app.flags.DEFINE_string('ckpt_path', '/model.ckpt-100000', '''模型保存路径''')
# tf.app.flags.DEFINE_float('learning_rate',0.0001,'''初始学习率''')
# tf.app.flags.DEFINE_integer('train_steps', 50000, '''总的训练轮数''')
# tf.app.flags.DEFINE_boolean('is_use_gpu', False, '''是否使用GPU''')
# print('模型保存路径： {}'.format(FLAGS.ckpt_path))
# print('初始学习率： {}'.format(FLAGS.learning_rate))
# print('总的训练次数： {}'.format(FLAGS.train_steps))
# print('是否使用GPU： {}'.format(FLAGS.is_use_gpu))


# E:\毕设\google map截图\road-extraction-d-linknet-master\
tf.app.flags.DEFINE_string(
    'summary_dir', 'E:\\毕设\\google map截图\\road-extraction-d-linknet-master\\summary',
    'path to store summary')
print('模型保存路径： {}'.format(FLAGS.summary_dir))

print(os.path.isdir('E:\\毕设\\google map截图\\road-extraction-d-linknet-master'))

# assert os.path.isdir(FLAGS.summary_dir),\
#         'Error, summary_dir must be a directory.'




# tf.app.flags.DEFINE_string("param_name", "default_val", '''description''')
# tf.app.flags.DEFINE_string("train_data_path", "/home/yongcai/chinese_fenci/train.txt", '''training data dir''')
# # tf.app.flags.DEFINE_string("log_dir", "E:/毕设/google map截图/road-extraction-d-linknet-master/logs", '''the log dir''')
# tf.app.flags.DEFINE_integer("max_sentence_len", 80, '''max num of tokens per query''')
# tf.app.flags.DEFINE_integer("embedding_size", 50, '''embedding size''')
# tf.app.flags.DEFINE_float("learning_rate", 0.001, '''learning rate''')
#
#
# def main(unused_argv):
#     train_data_path = FLAGS.train_data_path
#     print("train_data_path", train_data_path)
#     max_sentence_len = FLAGS.max_sentence_len
#     print("max_sentence_len", max_sentence_len)
#     embdeeing_size = FLAGS.embedding_size
#     print("embedding_size", embdeeing_size)
#     abc = tf.add(max_sentence_len, embdeeing_size)
#
#     init = tf.global_variables_initializer()
#
#     # with tf.Session() as sess:
#     # sess.run(init)
#     # print("abc", sess.run(abc))
#
#     sv = tf.train.Supervisor(logdir=FLAGS.log_dir, init_op=init)
#     with sv.managed_session() as sess:
#         print("abc:", sess.run(abc))
#
#         # sv.saver.save(sess, "/home/yongcai/tmp/")
#
#
# # 使用这种方式保证了，如果此文件被其他文件 import的时候，不会执行main 函数
# if __name__ == '__main__':
#     tf.app.run()  # 解析命令行参数，调用main 函数 main(sys.argv)