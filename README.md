# EnglishPosTagger

This is a tool meant for tagging words with their part-of-speech, a grammatical category based on their function within a sentence, such as noun, adjective, verb, and so forth. 

For Developers
============
You can also see [Java](https://github.com/starlangsoftware/EnglishPosTagger), [C++](https://github.com/starlangsoftware/EnglishPosTagger-CPP), or [C#](https://github.com/starlangsoftware/EnglishPosTagger-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called EnglishPosTagger will be created. Or you can use below link for exploring the code:

	git clone https://github.com/olcaytaner/EnglishPosTagger-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `EnglishPosTagger-Py` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 


## Compile

**From IDE**

After being done with the downloading and Maven indexing, select **Build Project** option from **Build** menu. After compilation process, user can run EnglishPosTagger-Py.

Detailed Description
============
+ [PosTagger](#postagger)

## PosTagger

İngilizce pos tagging için kullanılan PosTagger'ı eğitmek için 

	train(self, corpus: PosTaggedCorpus)
	
eğitilen PosTagger modelini kaydetmek için

	saveModel(self)
	
daha önce eğitilmiş bir PosTagger modelini yüklemek için

	loadModel(self)
	
ve yeni eğitilmiş veya yüklenmiş bir PosTagger modelini kullanarak bir cümleyi taglemek için

	posTag(self, sentence: Sentence) -> Sentence
	
metodu kullanılır.

3 farklı PosTagger modeli desteklenmektedir. Rasgele bir tag ile kelimeleri taglemek için kullanılan

	DummyPosTagger
	
o kelime için en çok kullanılan tag ile kelimeleri tagleyen

	NaivePosTagger
	
ve Hmm tabanlı bir eğitim yapıp buna göre kelimeleri tagleyen

	HmmPosTagger
