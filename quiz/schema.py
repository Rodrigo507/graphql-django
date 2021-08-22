import graphene
from graphene.types import schema
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes, Category, Question, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id','name')

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id','title','category','quiz')

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title','quiz')

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('question','answer_text')

class Query(graphene.ObjectType):
    all_questions = graphene.Field(QuestionType,id=graphene.Int())
    all_answers = graphene.List(AnswerType, id = graphene.Int())
    # all_quizzes = graphene.List(QuizzesType)
    # all_questions = graphene.List(QuestionType)

    def resolve_all_questions(root,info, id):
        return Question.objects.get(pk = id)
    
    def resolve_all_answers(root,info, id):
        return Answer.objects.filter(question = id)


    # def resolve_all_questions(root,info):
    #     return Question.objects.all()
    
    # quiz = graphene.String()
    # def resolve_quiz(parent,info):
    #     return f"This is the first question {self}"

schema = graphene.Schema(query = Query)