languages = ['C','CPP','JAVA','PYTHON','PERL','PHP','RUBY','CSHARP','HASKELL','CLOJURE','BASH','SCALA','ERLANG','CLISP','LUA','BRAINFUCK','JAVASCRIPT','GO','D','OCAML','R','PASCAL','SBCL','DART','GROOVY','OBJECTIVEC']
# regex = r"[1-9]\d{3,4}\s(C(?!.)|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D(?!.)|OCAML|R(?!.)|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)"
N = int(raw_input())

for _ in xrange(N):
    line = raw_input().split(' ')
    api_id, lang = int(line[0]), line[1]
    if ((api_id >= 10000) and (api_id < 100000) and (lang in languages)):
        print 'VALID'
    else:
        print 'INVALID'
