中山大学data
{
    Tables{
    comment{
    Columns{
    id
    author
    time
    post_id
    }

    Indexes{
    PRIMARY
    post_id
    }

    Foreign Keys{
    comment_ibfk_1
    }

    Triggers

    }

    post{
    Columns{
    id
    floor
    author
    content
    time
    comment_num
    thread_id
    }

    Indexes{
    PRIMARY
    thread_id
    }

    Foreign Keys{
    post_ibfk_1
    }

    Triggers
    }

    thread{
    Columns{
    id
    title
    author
    reply_num
    good
    }

    Indexes{
    PRIMARY
    }

    Foreign Keys{}

    Triggers{}

    }

    }

    Views

    Stored Procedures

    Functions
}