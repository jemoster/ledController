// Include gulp
var gulp = require('gulp');

// Include Our Plugins
var jshint = require('gulp-jshint');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var react = require('gulp-react');
var uglify = require('gulp-uglify');

// Lint Task
gulp.task('lint', function () {
    return gulp.src(['js/*.js', '!./js/debug/*.js'])
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

gulp.task('react-compile', function () {
    return gulp.src('js/*.jsx')
        .pipe(react())
        .pipe(gulp.dest('dist'));
});

// Concatenate & Minify JS
gulp.task('scripts', function () {
    return gulp.src(['js/*.js', '!./js/debug/*.js'])
        .pipe(uglify())
        .pipe(gulp.dest('dist'));
});

// Watch Files For Changes
gulp.task('watch', function () {
    gulp.watch('js/*.js', ['lint', 'scripts']);
    gulp.watch('js/*.jsx', ['react-compile']);
});

// Default Task
gulp.task('default', ['react-compile', 'scripts', 'watch']);