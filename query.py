import spacy
from graphene import ObjectType, Field, String

from schema import NLP, Doc, Token, Span, Cat, Meta


MODELS = {}


def get_model(name: str):
    if name not in MODELS:
        MODELS[name] = spacy.load(name)
    return MODELS[name]


def get_token(token: spacy.tokens.Token) -> Token:
    return Token(
        text=token.text,
        text_with_ws=token.text_with_ws,
        orth=token.orth,
        i=token.i,
        idx=token.idx,
        head_i=token.head.i,
        lower=token.lower,
        lower_=token.lower_,
        shape=token.shape,
        shape_=token.shape,
        lemma=token.lemma,
        lemma_=token.lemma_,
        norm=token.norm,
        norm_=token.norm_,
        pos=token.pos,
        pos_=token.pos_,
        tag=token.tag,
        tag_=token.tag_,
        dep=token.dep,
        dep_=token.dep_,
        ent_type=token.ent_type,
        ent_type_=token.ent_type_,
        ent_iob=token.ent_iob,
        ent_iob_=token.ent_iob,
        is_alpha=token.is_alpha,
        is_ascii=token.is_ascii,
        is_digit=token.is_digit,
        is_lower=token.is_lower,
        is_upper=token.is_upper,
        is_title=token.is_title,
        is_punct=token.is_punct,
        is_left_punct=token.is_left_punct,
        is_right_punct=token.is_right_punct,
        is_space=token.is_space,
        is_bracket=token.is_bracket,
        is_quote=token.is_quote,
        is_stop=token.is_stop,
        like_num=token.like_num,
        like_url=token.like_url,
        like_email=token.like_email
    )


def get_span(span: spacy.tokens.Span) -> Span:
    return Span(
        text=span.text,
        text_with_ws=span.text_with_ws,
        start=span.start,
        end=span.end,
        start_char=span.start_char,
        end_char=span.end_char,
        label=span.label,
        label_=span.label_
    )


def get_cat(label: str, score: float) -> Cat:
    return Cat(label=label, score=score)


def get_meta(meta: dict) -> Meta:
    return Meta(
        lang=meta.get('lang'),
        name=meta.get('name'),
        license=meta.get('license'),
        author=meta.get('author'),
        url=meta.get('url'),
        email=meta.get('email'),
        description=meta.get('description'),
        pipeline=meta.get('pipeline'),
        sources=meta.get('sources')
    )


def get_doc(doc):
    tokens = [get_token(token) for token in doc]
    ents = [get_span(ent) for ent in doc.ents]
    sents = [get_span(sent) for sent in doc.sents]
    cats = [get_cats(label, score) for label, score in doc.cats.items()]
    return Doc(
        text=doc.text,
        text_with_ws=doc.text_with_ws,
        tokens=tokens,
        ents=ents,
        sents=sents,
        cats=cats
    )


class Query(ObjectType):
    nlp = Field(NLP,
        text=String(required=True, description="The text to process"),
        model=String(required=True, description="The name of the model to use"),
        description="The nlp object used to process a text"
    )

    def resolve_nlp(self, info, text, model):
        _nlp = get_model(model)
        meta = get_meta(_nlp.meta)
        doc = get_doc(_nlp(text))
        return NLP(doc=doc, meta=meta)
