import React from 'react';
import { Link } from 'react-router-dom';


const home = () => (
    <div className="container">
        <div className="jumbotron my-3">
            <h3 className="display-4">Job Watcher here to serve you!</h3>
            <p className="lead">We alert you about all the updates you need in your everyday life. </p>
            <hr className="my-4" />
            <p>Click the button below to check out what's Trending today in the Job market.</p>
            <Link className="btn btn-primary btn-lg" exact to='/blog' role="button">Check for Trending Jobs</Link>
        </div>
    </div>
)

export default home;