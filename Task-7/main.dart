import 'package:flutter/material.dart';
import 'dart:async';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext c) {
    return MaterialApp(home: WordGame());
  }
}

class WordGame extends StatefulWidget {
  @override
  _WordGameState createState() => _WordGameState();
}

class _WordGameState extends State<WordGame> {
  List<String> words = ['rate', 'crate', 'night', 'thing', 'scape'];
  late String curWord;
  late String scrambled;
  int score = 0;
  int timeLeft = 20;
  Timer? timer;
  TextEditingController ctrl = TextEditingController();

  @override
  void initState() {
    super.initState();
    nextWord();
    startTimer();
  }

  void nextWord() {
    curWord = (words..shuffle()).first;
    scrambled = (curWord.split('')..shuffle()).join();
  }

  void startTimer() {
    timeLeft = 20;
    timer?.cancel();
    timer = Timer.periodic(Duration(seconds: 1), (t) {
      setState(() {
        timeLeft--;
        if (timeLeft <= 0) {
          timer?.cancel();
          showEndDialog();
        }
      });
    });
  }

  void showEndDialog() {
    showDialog(
      context: context,
      builder: (_) => AlertDialog(
        title: Text('Game Over'),
        content: Text('Score: $score'),
        actions: [
          TextButton(
            child: Text('Restart'),
            onPressed: () {
              Navigator.pop(context);
              setState(() {
                score = 0;
                nextWord();
                ctrl.clear();
                startTimer();
              });
            },
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext c) {
    return Scaffold(
      appBar: AppBar(title: Text('Word Rush')),
      body: Padding(
        padding: EdgeInsets.all(20),
        child: Column(
          children: [
            Text('Unscramble: $scrambled', style: TextStyle(fontSize: 24)),
            SizedBox(height: 10),
            Text('Time: $timeLeft', style: TextStyle(fontSize: 20)),
            TextField(
              controller: ctrl,
              decoration: InputDecoration(hintText: 'Your guess'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              child: Text('Submit'),
              onPressed: () {
                String guess = ctrl.text.toLowerCase().trim();
                if (guess == curWord.toLowerCase()) {
                  ctrl.clear();
                  setState(() {
                    score++;
                    nextWord();
                    timeLeft = 20;
                  });
                  startTimer();
                } else {
                  timer?.cancel();
                  showEndDialog();
                }
              },
            ),
            Spacer(),
            Text('Score: $score', style: TextStyle(fontSize: 20)),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    timer?.cancel();
    ctrl.dispose();
    super.dispose();
  }
}
