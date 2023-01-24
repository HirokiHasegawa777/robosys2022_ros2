# robosys2022_ros2
こちらは、千葉工業大学先進工学部未来ロボティクス学科2年4学期の講義で使用しているリポジトリです。  
本パッケージでは暗号文を作って擬似的に通信することが出来ます。
## ノードとトピックの概要
* sender
    * cryptogram.txtを読み込み、秘密鍵の数字の分だけasciiコードをずらすことで暗号文を作成。
* receiver
    * 暗号文と秘密鍵を受け取り、asciiコードのズレを戻すことで元の文章を復元。
* /chatter
    * String型の変数に暗号文と秘密鍵を格納
## 使い方
* まず、robosys2022_ros2ディレクトリにあるcryptogram.txtに暗号文の元となる文章を書き込み、保存します。ただし、日本語は入力不可。
* 次に、同様のディレクトリにあるsender.pyのself.keyの数字を必要に応じて0~9の範囲で設定します。
* ビルドして以下を実行すると暗号文と解読文が表示されます。
  ```
  $ ros2 launch robosys2022_ros2 cipher_launch.py
  ```
## 動作確認済み環境
* Ubuntu 20.04 LTS
* ROS2 noetic
## LICENSE
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。  
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。  
  * [ryuichiueda/my_slides robotsys2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2022 Hiroki Hasegawa